import pytest
# * Aquí se importa todos los artilugios generado de nuestro archivo de drivers!
# * Primero, se importa siempre "pytest" librería de Python para realizar pruebas (the best!)
# * A continuación, verás que los imports de nuestros archivos deben comenzar siempre desde el root directory "tests"
# * En el archivo testbase en especial, se alojan todos  los TestUtils para nuestras pruebas.
from tests.testbase import Locators, WebDriver, Drivers


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to use: chrome, edge, firefox",
        choices=("chrome", "edge", "firefox"),
    )


@pytest.fixture
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")


BROWSER_FUNCTIONS = {
    "chrome": Drivers().chromeDriver,
    "edge": Drivers().edgeDriver,
    "firefox": Drivers().firefoxDriver
}


@pytest.fixture
def setWebDriver(browser):
    if not isinstance(browser, str):
        raise ValueError(f'Invalid CLI parameter')
    # * Crear la instancia del Driver (dado el driver elegido por CLI):
    driver = BROWSER_FUNCTIONS.get(browser)
    if not driver:
        raise ValueError(f'Browser "{browser}" not supported.')

    runDriver: WebDriver = driver()
    if not isinstance(runDriver, WebDriver):
        raise ValueError(f'WebDriver was not instanced')

    return runDriver


@pytest.fixture
def web(setWebDriver):
    if not isinstance(setWebDriver, WebDriver):
        raise ValueError(f'WebDriver was not instanced')

    return setWebDriver


@pytest.fixture
def get(web):
    if not isinstance(web, WebDriver):
        raise ValueError(f'WebDriver was not instanced')
    # * Crear nueva instancia de las utilidades de prueba (test utils):
    get = Locators(web)
    if not isinstance(get, Locators):
        raise ValueError(f'Locators Class was not instanced')

    return get


# * ---- Fixture para usar como BeforeEach y AfterEach: abre y cierra el navegador ----
@pytest.fixture
def beforeEach(setWebDriver: WebDriver):
    if not isinstance(setWebDriver, WebDriver):
        raise ValueError(f'WebDriver was not instanced')

    web = setWebDriver
    get = Locators(web)
    # * ESTA ES UNA FORMA INTELIGENTE DE MANEJAR TUS PRUEBAS!
    # la forma más prolija que te puedo enseñar!
    # todo: Se obtiene la URL de Google y se verifica el título
    web.implicitly_wait(10)
    get.page("https://www.saucedemo.com/")

    # todo:  Se verifica el título de la página
    title = web.title
    assert title == "Swag Labs"

    # * Fin de la Precondición.
    # todo: Aquí puedes colocar el código que quieres retornar del setup.
    yield (web, get)
    # todo Código de la PostCondición.
    web.quit()  # Se cierra el navegador


if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
