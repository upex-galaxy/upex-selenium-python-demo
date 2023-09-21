# __________
# # * 🧪 ESTE es un archivo que puede englobar TODAS las interacciones con las pruebas, sobretodo la instancia del driver.
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.utils.drivers import Drivers


Test = tuple[WebDriver, Locators]
