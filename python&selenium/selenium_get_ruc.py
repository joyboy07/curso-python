from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from decouple import config
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chrome_driver_path = 'C:/Users/jporlles/Desktop/dev/curso-python/python&selenium/chromedriver-win32/chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

ruta_archivo = config('ENTRADA')
df = pd.read_excel(ruta_archivo)

def consulta_ruc(nombre):
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnPorRazonSocial"))).click()
        user = driver.find_element(By.ID, "txtNombreRazonSocial")
        user.clear()
        user.send_keys(nombre)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnAceptar"))).click()
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
            return None
        except TimeoutException:
            pass
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "list-group")))
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        maquinas = soup.find_all('a', class_='aRucs')
        if maquinas:
            ruc = maquinas[0]
            ruc_number = ruc['data-ruc']
            nombres = ruc.find_all('h4', class_='list-group-item-heading')
            if len(nombres) >= 2:
                nombre_ruc = nombres[1].get_text(strip=True)
                resultado = {
                    "empresa": nombre,
                    "rucEncontrado": ruc_number,
                    "desEcnontrado": nombre_ruc
                }
                return resultado
        else:
            print("No se encontraron resultados.")
            return None

    except TimeoutException:
        print("Tiempo de espera excedido.")
        return None
    finally:
        driver.quit()  # Asegurarse de cerrar el driver
        print("Proceso completado.")

def universidadPeru(nombre):
    try:
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.universidadperu.com/empresas/busqueda/")
        input = driver.find_element(By.ID, "buscaempresa1")
        input.clear()
        input.send_keys(nombre)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Buscar"]'))).click()
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, "html.parser")
        local_businesses = soup.find_all(attrs={"itemtype": "https://schema.org/LocalBusiness"})
        business_data = {}
        for business in local_businesses:
            for li in business.find_all('li'):
                strong_tag = li.find('strong')
                if strong_tag:
                    key = strong_tag.get_text(strip=True).replace(":", "")
                    value = li.get_text(strip=True).replace(strong_tag.get_text(strip=True), "").strip()
                    if value:
                        business_data[key] = value
        ruc = business_data.get("RUC", "")
        razon_social = business_data.get("Razón Social", "")
        resultado = {
            "empresa": nombre,
            "rucEncontrado": ruc,
            "desEcnontrado": razon_social
        }
        return resultado
    except TimeoutException:
        print("Saliio un error")
        driver.quit()


data ={
    'empresa':[],
    'rucEncontrado':[],
    'desEcnontrado':[]

}

for index, row in df.iterrows():
    resultado = consulta_ruc(row['Razón Social'])
    if resultado is None:
        resultado2 = universidadPeru(row['Razón Social'])
        data['empresa'].append(resultado2['empresa'])
        data['rucEncontrado'].append(resultado2['rucEncontrado'])
        data['desEcnontrado'].append(resultado2['desEcnontrado'])
    else:
        data['empresa'].append(resultado['empresa'])
        data['rucEncontrado'].append(resultado['rucEncontrado'])
        data['desEcnontrado'].append(resultado['desEcnontrado'])


df = pd.DataFrame(data)
ruta = config('SALIDA')
df.to_excel(ruta, index=False, engine='openpyxl')