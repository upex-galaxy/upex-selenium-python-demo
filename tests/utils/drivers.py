# -----
# * aquí se instancia todos los WebDrivers que se necesiten
import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOpt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOpt
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )


@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")


class Drivers:

    def __init__(self, isHeadless=False) -> None:
        self.isHeadless = isHeadless

    def chromeDriver(self):
        # *  Se crea una instancia del Chrome
        if self.isHeadless == True:
            execution = ChromeOpt()
            execution.add_argument("--headless")
            return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=execution)
        else:
            return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

    def edgeDriver(self):
        # *  Se crea una instancia del Microsoft Edge
        if self.isHeadless == True:
            execution = EdgeOpt()
            execution.add_argument("--headless")
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=execution)
        else:
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def firefoxDriver(self):
        # *  Se crea una instancia del FireFox
        if self.isHeadless == True:
            execution = FirefoxOpt()
            execution.add_argument("--headless")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=execution)
        else:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


if __name__ == "__main__":
    pytest.main()
