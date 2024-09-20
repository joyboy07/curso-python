import shutil

ruta_origen = 'D:/gatos/gata.txt'
ruta_destino = 'ruta/de/destino/gata.txt'

shutil.copy(ruta_origen, ruta_destino)

print("Archivo copiado con éxito")