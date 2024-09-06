import requests
from bs4 import BeautifulSoup

# url = 'https://serviciosweb.osiptel.gob.pe/ConsultaSIRT/Buscar/FrmVerTarifa.aspx?pTarifa=157089'
url = 'https://dockerlabs.es/'
respuesta = requests.get(url)

if respuesta.status_code == 200:
	soup = BeautifulSoup(respuesta.text, 'html.parser')
	maquinas = soup.find_all('button', class_='upload')
	print(maquinas)


	# for maquina in maquinas:
	# 	onclick_text = maquina['onclick']
	# 	nombre_maquina = onclick_text.split("'")[1]
	# 	print(nombre_maquina)
else:
	print(f'Hubo un error al hcer la peticion {respuesta.status_code}')
