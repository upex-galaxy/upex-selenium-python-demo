from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Locators:
    # * Definición de funciones para interactuar con elementos de la página
    def __init__(self, driver: WebDriver):
        self.web = driver

    def page(self, link: str):
        # Función para abrir una URL en el navegador web y maximizar la ventana
        self.web.maximize_window()
        self.web.get(link)

    def byDataTest(self, data_test: str):
        # Buscar elemento por data-test id
        return self.web.find_element(By.CSS_SELECTOR, f"[data-test={data_test}]")

    def byDataTests(self, data_test: str):
        # Buscar elemento por data-test ids
        return self.web.find_elements(By.CSS_SELECTOR, f"[data-test={data_test}]")

    def bySelector(self, element: str):
        # Buscar elemento por selector CSS
        return self.web.find_element(By.CSS_SELECTOR, element)

    def bySelectors(self, element: str):
        # Buscar elemento por selector CSS
        return self.web.find_elements(By.CSS_SELECTOR, element)

    def byTag(self, element: str):
        # Buscar elemento por nombre de etiqueta
        return self.web.find_element(By.TAG_NAME, element)

    def byTags(self, element: str):
        # Buscar elemento por nombre de etiqueta
        return self.web.find_elements(By.TAG_NAME, element)

    def byID(self, element: str):
        # Buscar elemento por ID
        return self.web.find_element(By.ID, element)

    def byIDs(self, element: str):
        # Buscar elemento por ID
        return self.web.find_elements(By.ID, element)

    def byClass(self, element: str):
        # Buscar elemento por nombre de clase
        return self.web.find_element(By.CLASS_NAME, element)

    def byClasses(self, element: str):
        # Buscar elemento por nombre de clase
        return self.web.find_elements(By.CLASS_NAME, element)

    def byName(self, element: str):
        # Buscar elemento por nombre
        return self.web.find_element(By.NAME, element)

    def byNames(self, element: str):
        # Buscar elemento por nombre
        return self.web.find_elements(By.NAME, element)

    def byXpath(self, element: str):
        # Buscar elemento por XPath
        return self.web.find_element(By.XPATH, element)

    def byXpaths(self, element: str):
        # Buscar elemento por XPath
        return self.web.find_elements(By.XPATH, element)

    # * ---- Smart Locators

    def contains(self, text: str):
        # Buscar element por dado innerText como contenedor (no estricto)
        return self.web.find_elements(By.XPATH, f'//*[contains(text(),"{text}")]')

    def withinElement_get(self, parentElement: WebElement, childElement: str):
        # Buscar un element específico dentro de un elemento padre
        return parentElement.find_element(By.CSS_SELECTOR, childElement)
