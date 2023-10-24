import pytest
from tests.testbase import *
from tests.pages.exampleLoginPage import LoginPage
from tests.pages.GX_40963_FooterPage import FooterPage


def initialSetup():
    global get, web, loginPage, swgPLPPage, footerPage
    web = Drivers().chromeDriver()
    get = Locators(web)
    loginPage = LoginPage(web, get)
    footerPage = FooterPage(web, get)


def loginPrecondition():
    get.page('https://www.saucedemo.com/')
    loginPage.enterUsername(inputValue='standard_user')
    loginPage.enterPassword(inputValue='secret_sauce')
    loginPage.submitLogin()
    Url = web.current_url
    assert '/inventory' in Url


@pytest.fixture
def beforeEach():
    initialSetup()
    loginPrecondition()


def test_TC01(beforeEach):
    footerPage.clickLink(targetLink='twitter')
