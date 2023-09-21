import pytest
from tests.testbase import *


# * EJEMPLO CON PAGE OBJECT MODEL con todo! Aquí primero hay que importar el módulo POM que se desea usar (o también los necesarios)
from tests.how_to.pages.examplePageObjectModel import ExampleLoginPage


class TestLoginSauce:

    @pytest.fixture
    def precondition(self):
        # Se listan las variables globales del Suite de Prueba.
        global web, get, loginPage
        web = Drivers().chromeDriver()
        get = Locators(web)
        loginPage = ExampleLoginPage(web, get)
        get.page('https://www.saucedemo.com/')

    # * Si se necesita precondiciones específicas, se puede agregar más Fixtures luego de correr las otras:
    @pytest.fixture
    def givenUserCredentials(self, precondition):
        validUsername = loginPage.getLoginUserValue()
        validPassword = loginPage.getLoginPasswordValue()

        yield validUsername, validPassword
        web.quit()

    def test_login_success(self, givenUserCredentials):
        if not isinstance(givenUserCredentials, tuple[str, str]):
            raise ValueError()
        validUsername, validPassword = givenUserCredentials
        loginPage.enterUsername(username=validUsername)
        loginPage.enterPassword(password=validPassword)
        loginPage.submitLogin()

        url = web.current_url
        assert "inventory.html" in url


if __name__ == "__main__":
    pytest.main()