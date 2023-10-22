from tests.testbase import *


class SwagLabPLP:
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver
        self.get = locator
        self.dropdownFilterProducts = lambda: self.get.byDataTest(
            'product_sort_container')
        self.listItemsPLP = lambda: self.get.bySelectors(
            '[class="inventory_item"]')
        self.itemNameList = lambda: self.get.bySelectors(
            '[class="inventory_item_name "]')
        self.itemPriceList = lambda: self.get.bySelectors(
            '[class="inventory_item_price"]')

    def getDefaultFilterProducts(self):
        items = []
        for index in range(len(self.listItemsPLP())):
            itemName = self.itemNameList()[index].text
            itemPrice = self.itemPriceList()[index].text
            items.append([itemName, itemPrice])
        return items
