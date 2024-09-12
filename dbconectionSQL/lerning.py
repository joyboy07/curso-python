import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [28, 34, 45],
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo']
}
df = pd.DataFrame(data)

ruta = '//killari/Unidad_Informatica/Desarrollo/comext/fat.xlsx'  # Cambia esto a la ruta donde quieres guardar el archivo
df.to_excel(ruta, index=False, engine='openpyxl')
