from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

#abrir pagina
chrome_driver_path = 'C:/Users/jporlles/Desktop/dev/curso-python/python&selenium/chromedriver-win32/chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://serviciosweb.osiptel.gob.pe/ConsultaSIRT/Buscar/frmConsultaTar.aspx")

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnBv"))).click()

# Selector Tipo de Tarifa

def click_element_with_retry(driver, select_id, xpath, retries=3):
    for i in range(retries):
        try:
            dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, select_id))
            )
            dropdown.click()

            option_to_select = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            option_to_select.click()
            break
        except StaleElementReferenceException:
            print(f"Intento {i+1}: Elemento ya no es válido. Reintentando...")
            continue
click_element_with_retry(driver, "ddlVigente", "//option[normalize-space(text())='[Vigente y No Vigentes]']")

#Periodo de vigencia
	#desde
txtFechaIniVig = driver.find_element(By.NAME,"txtFechaIniVig")
txtFechaIniVig.clear()
txtFechaIniVig.send_keys("01/01/2019")
	#hasta
txtFechaFinVig = driver.find_element(By.NAME,"txtFechaFinVig")
txtFechaFinVig.clear()
txtFechaFinVig.send_keys("28/02/2019")

# Buscar123 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Buscar123"))).click()

time.sleep(40)