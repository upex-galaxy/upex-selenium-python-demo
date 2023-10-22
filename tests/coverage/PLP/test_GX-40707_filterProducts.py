import pytest
from tests.testbase import *
from tests.pages.GX_40707_LoginPage import LoginPage


def initialSetup():
    global get, web, loginPage
    web = Drivers().chromeDriver()
    get = Locators(web)
    loginPage = LoginPage(web, get)


def loginPrecondition():
    get.page('https://www.saucedemo.com/')
    loginPage.login(username='standard_user', password='secret_sauce')
    loginPage.clickButtonSubmit()
    Url = web.current_url
    assert '/inventory' in Url


@pytest.fixture
def beforeEach():
    initialSetup()
    loginPrecondition()


def test_TC01(beforeEach):
    pass
