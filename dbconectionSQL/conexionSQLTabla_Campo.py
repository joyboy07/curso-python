import pymssql
import pandas as pd

# Datos de conexión

server = '192.168.201.212'  # Por ejemplo: 'localhost' o 'mi_servidor'
database = 'DNCN_ComercioExt'
username = 'sa'
password = ''

try:
    conn = pymssql.connect(server, username, password, database)
    print("Conexión exitosa.")
    cursor = conn.cursor()

    tablas =["a101","AcumulateVar","ANIO","comextma_admision","comextma_correlacion","comextma_exportacion","comextma_importacion3","comextma_N365","comextma_ndoc","comextma_ndoc_impo","comextma_partidas","comextma_reglas","comextma_variable","comextma_variable_at","comextma_variable_imp","comextma_variable_zf","comextma_zfranca","comextpro_admision","comextpro_anexos","comextpro_exportacion","comextpro_exportacion_CPartida","comextpro_importacion3","comextpro_zfranca","correlacion","RMPro_BP_Datos","RMPro_SumDatosExp","RMpro_SumDatosImp","TablaD_C","TablaD_T"]
    data ={
        'Tablas':[],
        'Campo':[]
	}

    for row in tablas:
        cursor.execute(f"""
			SELECT
				COLUMN_NAME AS NombreColumna
			FROM
				INFORMATION_SCHEMA.COLUMNS
			WHERE
				TABLE_NAME = '{row}'
				AND TABLE_SCHEMA = 'dbo'
			ORDER BY
				ORDINAL_POSITION;
		""")
        results = cursor.fetchall()
        for j in results:
                        data['Tablas'].append(row)
                        data['Campo'].append(j[0])
                        print('Procesando..')

    df = pd.DataFrame(data)
    ruta = '//killari/Unidad_Informatica/Desarrollo/comext/analisisPythonTablaCampo.xlsx'
    df.to_excel(ruta, index=False, engine='openpyxl')

except pymssql.Error as e:
    print("Error en la conexión:", e)

finally:
    if conn:
        conn.close()
        print("Conexión cerrada.")