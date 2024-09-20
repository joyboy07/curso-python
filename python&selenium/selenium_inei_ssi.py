from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

#abrir pagina
chrome_driver_path = 'C:/Users/jporlles/Desktop/dev/curso-python/python&selenium/chromedriver-win32/chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://webapp.inei.gob.pe/ssi/Login")


# llenar formulario
## llenamos el input usuario
user = driver.find_element(By.ID,"username")
user.clear()
user.send_keys("jporlles")
## llenamos el input contrasenia
password = driver.find_element(By.ID,"clave")
password.clear()
password.send_keys("76934958")


input_element = driver.find_element(By.ID, "a")
default_value = input_element.get_attribute("value")

resultado = driver.find_element(By.ID,"b")
resultado.clear()
resultado.send_keys(eval(default_value))

#Ingresamos a la web
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_ingresar"))).click()

#Ingresamos a la siguiente pagina
li_element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CLASS_NAME, "n_01")))
enlace = li_element.find_element(By.TAG_NAME, "a")
enlace.click()
#llenamos el siguiente formulario

##sselector 1
input_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.custom-combobox-input'))
)
input_element.clear()
input_element.send_keys('Otros')

title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'titulo'))
)
title.clear()
title.send_keys('Otros')

##Selector 2
dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection__arrow"))
)

dropdown_button.click()
option_to_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Sede Central')]"))  # Cambia por el texto visible de la opción
)
option_to_select.click()

desciption = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'descripcion_incidencia'))
)
desciption.clear()
desciption.send_keys('Requiero el apoyo para la habilitacion de aplicativo docker')

buttonInsidencia = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'btn_guardar_inc'))
)
buttonInsidencia.click()
time.sleep(10)
#