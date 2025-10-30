from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\tmaquinaria\Desktop\VIC\GIT\Proyectos_Python\Recepcion_Mensaje_Wpp\DatosUser")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.github.com')

time.sleep(20)