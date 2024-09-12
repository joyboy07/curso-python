import pymssql
import pandas as pd

# Datos de conexión

server = ''  # Por ejemplo: 'localhost' o 'mi_servidor'
database = 'DNCN_ComercioExt'
username = 'sa'
password = ''

try:
    conn = pymssql.connect(server, username, password, database)
    print("Conexión exitosa.")
    cursor = conn.cursor()

    cursor.execute("""
		SELECT
			t.name AS TablaNombre
		FROM
			sys.tables t
		INNER JOIN
			sys.schemas s
			ON t.schema_id = s.schema_id
		WHERE
			s.name = 'dbo'
			AND t.name NOT IN ('sysdiagrams', 'dtproperties')
		ORDER BY
			t.name;
	""")
    rows = cursor.fetchall()
    data ={
        'Tablas':[],
        'Procedimientos':[]
	}
    for row in rows:
        cursor.execute(f"""
			SELECT
				p.name AS ProcedimientoNombre
			FROM
				sys.procedures AS p
			INNER JOIN
				sys.sql_modules AS m
				ON p.object_id = m.object_id
			WHERE
				m.definition LIKE '%{row[0]}%'
		""")
        results = cursor.fetchall()
        if len(results) != 0:
            # print(row[0],"--")
            for j in results:
                print('Procesando..')
                data['Tablas'].append(row[0])
                data['Procedimientos'].append(j[0])

    df = pd.DataFrame(data)
    ruta = '//killari/Unidad_Informatica/Desarrollo/comext/analisisPython.xlsx'
    df.to_excel(ruta, index=False, engine='openpyxl')

except pymssql.Error as e:
    print("Error en la conexión:", e)

finally:
    if conn:
        conn.close()
        print("Conexión cerrada.")