import pymssql
import pandas as pd
from decouple import config

# Datos de conexión

server = config('HOST')  # Por ejemplo: 'localhost' o 'mi_servidor'
database = 'CPI'
username = 'sa'
password = config('PASSWORD')

try:

    ruta_archivo = '//killari/Unidad_Informatica/Desarrollo/ccp/data-codificada/data_prueba.xlsx'
    df = pd.read_excel(ruta_archivo)

    conn = pymssql.connect(server, username, password, database)
    print("Conexión exitosa.")
    cursor = conn.cursor()
    conn.autocommit(False)

    duplicates =[]

    def saveDuplicates(id_producto, id_establecimiento):
        duplicate_entry = {
            'id_producto': id_producto,
            'id_establecimiento': id_establecimiento
        }
        duplicates.append(duplicate_entry)

    def exisEmpresa(ruc,rsocial):
        cursor.execute("SELECT COUNT(*) FROM empresa WHERE id = %s", (ruc,))
        exisEmpresa = cursor.fetchone()[0] > 0
        if not exisEmpresa:
            cursor.execute("INSERT INTO empresa(id, razon_social) VALUES (%s, %s)", (ruc, rsocial))

    def exisEstablecimiento(ruc, numeroEstabl, rsocilEsta, id_ciiu4 ):
        cursor.execute("SELECT COUNT(*) FROM establecimiento WHERE id = %s", (ruc+numeroEstabl))
        exis = cursor.fetchone()[0] > 0
        if not exis:
            cursor.execute("INSERT INTO establecimiento  (id ,numero ,razon_social ,id_empresa ,id_ciiu4) VALUES (%s,%s,%s,%s,%s)",(ruc+numeroEstabl, numeroEstabl, rsocilEsta, ruc, id_ciiu4))

    def exisProducto(producto, id_ccp, id_product):
        cursor.execute("SELECT id FROM producto WHERE descripcion = %s", (producto,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute(
                "INSERT INTO producto(descripcion, id_ccp, id_producto373, id_usuario) VALUES (%s, %s, %s, %s)",
                (producto, id_ccp, id_product, '12345678')
            )
            return cursor.lastrowid
        else:
            return result[0]

    def insertProductoEstablecimiento(id_producto, id_establecimiento, id_tipoProudcto):
        try:
            cursor.execute(
                "INSERT INTO producto_establecimiento (id_producto,id_establecimiento,id_productoEstablecimientoTipo) VALUES (%s, %s, %s)",
                (id_producto, id_establecimiento, id_tipoProudcto)
            )
        except pymssql.Error as e:
            sqlstate = e.args[0]
            if sqlstate == 2627:
                saveDuplicates(id_producto,id_establecimiento)

    for index, row in df.iterrows():
        exisEmpresa(str(row['ruc']),'-')
        exisEstablecimiento(str(row['ruc']),str(row['numero_establecimiento']),'-','0311')
        resul = exisProducto(row['nombre_producto'],str(row['cod_ccp']),str(row['cod_n']))
        insertProductoEstablecimiento(resul, str(row['ruc'])+str(row['numero_establecimiento']),row['tipo_producto'])

    print(duplicates)

    conn.commit()

except pymssql.Error as e:
    conn.rollback()
    print("Error en la conexióna:", e)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexión cerrada.")