import pytest
from tests.testbase import *
from tests.pages.GX_40707_PLPPage import SwagLabPLP
from tests.pages.GX_40707_LoginPage import LoginPage


def initialSetup():
    global get, web, loginPage, swgPLPPage
    web = Drivers().chromeDriver()
    get = Locators(web)
    loginPage = LoginPage(web, get)
    swgPLPPage = SwagLabPLP(web, get)


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


def test_TC01_filter_name_products_Descendent(beforeEach):
    currentVal = swgPLPPage.getCurrentFilterProducts()
    sortedNamesDesc = swgPLPPage.sortedProducts(
        listToSort=currentVal, targetValue=0, reverseOption=True)
    for itemDefault, itemDesc in zip(currentVal, sortedNamesDesc):
        itemNameDefault = itemDefault[0]
        itemNameDesc = itemDesc[0]
        expect(itemNameDefault).toNotBeEqual(itemNameDesc)


def test_TC02_filter_name_products_Ascendent(beforeEach):
    swgPLPPage.filterProduct(targetFilterOption=1)
    currentVal = swgPLPPage.getCurrentFilterProducts()
    sortedNamesAsc = swgPLPPage.sortedProducts(
        listToSort=currentVal, targetValue=0, reverseOption=False)
    for itemDefault, itemAsc in zip(currentVal, sortedNamesAsc):
        itemNameDefault = itemDefault[0]
        itemNameAsc = itemAsc[0]
        expect(itemNameDefault).toNotBeEqual(itemNameAsc)


def test_TC03_filter_price_products_Ascendent(beforeEach):
    swgPLPPage.filterProduct(targetFilterOption=3)
    currentVal = swgPLPPage.getCurrentFilterProducts()
    sortedPricesAsc = swgPLPPage.sortedProducts(
        listToSort=currentVal, targetValue=1, reverseOption=False)
    sortedPricesAsc = sortedPricesAsc[::-1]
    for itemDefault, itemAsc in zip(currentVal, sortedPricesAsc):
        itemPriceDefault = itemDefault[1]
        itemPriceAsc = itemAsc[1]
        expect(itemPriceDefault).toBeEqual(itemPriceAsc)


def test_TC04_filter_price_products_Descendent(beforeEach):
    swgPLPPage.filterProduct(targetFilterOption=2)
    currentVal = swgPLPPage.getCurrentFilterProducts()
    sortedPricesDesc = swgPLPPage.sortedProducts(
        listToSort=currentVal, targetValue=1, reverseOption=True)
    sortedPricesDesc = sortedPricesDesc[::-1]
    for itemDefault, itemDesc in zip(currentVal, sortedPricesDesc):
        itemPriceDefault = itemDefault[1]
        itemPriceDesc = itemDesc[1]
        expect(itemPriceDefault).toBeEqual(itemPriceDesc)
