# 🧪 ESTE es un archivo que puede englobar TODAS las interacciones con las pruebas, sobretodo la instancia del driver.
# * aquí se instancia el WebDriver, y además se declaran algunos TestUtils para usar en las pruebas y facilitar el manejo de métodos repetitivos.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver

# *  Se crea una instancia del ChromeDriver


def chromeDriver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# * Definición de funciones para interactuar con elementos de la página
class Locators:
    def __init__(self, driver: WebDriver):
        self.web = driver

    def goto(self, link: str):
        # Función para abrir una URL en el navegador web y maximizar la ventana
        self.web.maximize_window()
        self.web.get(link)

    def getSelector(self, element: str):
        # Buscar elemento por selector CSS
        return self.web.find_element(By.CSS_SELECTOR, element)

    def getTag(self, element: str):
        # Buscar elemento por nombre de etiqueta
        return self.web.find_element(By.TAG_NAME, element)

    def getID(self, element: str):
        # Buscar elemento por ID
        return self.web.find_element(By.ID, element)

    def getClass(self, element: str):
        # Buscar elemento por nombre de clase
        return self.web.find_element(By.CLASS_NAME, element)

    def getName(self, element: str):
        # Buscar elemento por nombre
        return self.web.find_element(By.NAME, element)

    def getXpath(self, element: str):
        # Buscar elemento por XPath
        return self.web.find_element(By.XPATH, element)


if __name__ == "__main__":
    pytest.main()
