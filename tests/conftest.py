import pytest
# * Aquí se importa todos los artilugios generado de nuestro archivo de drivers!
# * Primero, se importa siempre "pytest" librería de Python para realizar pruebas (the best!)
# * A continuación, verás que los imports de nuestros archivos deben comenzar siempre desde el root directory "tests"
# * En el archivo testbase en especial, se alojan todos  los TestUtils para nuestras pruebas.
from selenium.webdriver.remote.webdriver import WebDriver
from tests.testbase import *
from tests.utils.asserts import Expect
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to use: chrome, edge, firefox",
        choices=("chrome", "edge", "firefox"),
    )
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )


@pytest.fixture
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")


@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")


@pytest.fixture
def setWebDriver(headless: str, browser: str):
    # * Convertir el valor de headless a boolean:
    run = True if headless == "true" else False
    # * Crear la instancia del Driver (dado el driver elegido por CLI):
    BROWSER_FUNCTIONS = {
        "chrome": Drivers(run).chromeDriver,
        "edge": Drivers(run).edgeDriver,
        "firefox": Drivers(run).firefoxDriver
    }
    driver = BROWSER_FUNCTIONS.get(browser)
    if not driver:
        raise ValueError(f'Browser "{browser}" not supported.')

    runDriver: WebDriver = driver()
    return runDriver


@pytest.fixture
def web(setWebDriver: WebDriver):
    # * Obtener solamente la instancia del WebDriver
    return setWebDriver


@pytest.fixture
def get(web: WebDriver):
    # * Crear nueva instancia de las utilidades de prueba (test utils):
    get = Locators(web)
    return get


# * ---- Fixture para usar como BeforeEach y AfterEach: abre y cierra el navegador ----
@pytest.fixture
def setup(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)
    # * ESTA ES UNA FORMA INTELIGENTE DE MANEJAR TUS PRUEBAS!
    # la forma más prolija que te puedo enseñar!
    # todo: Se obtiene la URL de Google y se verifica el título
    web.implicitly_wait(10)
    get.page("https://google.com")

    # todo:  Se verifica el título de la página
    title = web.title
    assert title == "Google"

    # * Fin de la Precondición.
    # todo: Aquí puedes colocar el código que quieres retornar del setup.
    yield (web, get)
    # todo Código de la PostCondición.
    web.quit()  # Se cierra el navegador


@pytest.fixture
def beforeEach(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)
    web.implicitly_wait(10)
    get.page("https://www.saucedemo.com/")
    title = web.title
    assert title == "Swag Labs"
    yield (web, get)
    web.quit()


@pytest.fixture
def validUser():
    data = {
        "username": "standard_user",
        "password": "secret_sauce"
    }
    return data


@pytest.fixture
def loginSuccessful(beforeEach: Test, validUser: dict[str, str]):
    web, get = beforeEach
    loginPage = exLoginPage(web, get)
    loginPage.enterUsername(validUser["username"])
    loginPage.enterPassword(validUser["password"])
    loginPage.submitLogin()
    expect(web.current_url).toContain("/inventory")
    yield (web, get)


if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
