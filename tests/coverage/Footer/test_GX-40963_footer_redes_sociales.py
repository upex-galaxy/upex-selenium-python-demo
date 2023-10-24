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
    global defaultTab
    initialSetup()
    loginPrecondition()
    defaultTab = web.current_window_handle


def test_TC1_acceder_red_social_twitter(beforeEach):
    footerPage.clickLink(targetLink='twitter')
    footerPage.switchNewTab(defaultTab=defaultTab)
    newCurrentTab = web.current_url
    assert 'twitter' in newCurrentTab
