import pytest
import requests
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
    global defaultTab, headers
    initialSetup()
    loginPrecondition()
    defaultTab = web.current_window_handle
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }


def test_TC1_acceder_red_social_twitter(beforeEach):
    hrefValue = footerPage.getHrefAttrib(targetLink='twitter')
    response = requests.get(f'{hrefValue}')
    footerPage.clickLink(targetLink='twitter')
    footerPage.switchNewTab(defaultTab=defaultTab)
    newCurrentTab = web.current_url
    expect(response.status_code).toBeEqual(200)
    assert 'twitter' in newCurrentTab


def test_TC2_acceder_red_social_facebook(beforeEach):
    hrefValue = footerPage.getHrefAttrib(targetLink='facebook')
    response = requests.get(f'{hrefValue}')
    footerPage.clickLink(targetLink='facebook')
    footerPage.switchNewTab(defaultTab=defaultTab)
    newCurrentTab = web.current_url
    expect(response.status_code).toBeEqual(200)
    assert 'facebook' in newCurrentTab


def test_TC3_acceder_red_social_linkedIn(beforeEach):
    hrefValue = footerPage.getHrefAttrib(targetLink='linkedin')
    response = requests.get(f'{hrefValue}', headers=headers)
    footerPage.clickLink(targetLink='linkedin')
    footerPage.switchNewTab(defaultTab=defaultTab)
    newCurrentTab = web.current_url
    expect(response.status_code).toBeEqual(200)
    assert 'linkedin' in newCurrentTab
