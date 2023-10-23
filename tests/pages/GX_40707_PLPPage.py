from tests.testbase import *
from selenium.webdriver.support.select import Select


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

    def getCurrentFilterProducts(self):
        items = []
        for index in range(len(self.listItemsPLP())):
            itemName = self.itemNameList()[index].text
            itemPrice = self.itemPriceList()[index].text.replace('$', '')
            items.append([itemName, float(itemPrice)])
        return items

    def sortedProducts(self, listToSort, targetValue, reverseOption):
        itemNameSorted = sorted(
            listToSort, key=lambda x: x[targetValue], reverse=reverseOption)
        return itemNameSorted

    def filterProduct(self, targetFilterOption):
        dropdown = Select(self.dropdownFilterProducts())
        dropdown.select_by_index(targetFilterOption)
