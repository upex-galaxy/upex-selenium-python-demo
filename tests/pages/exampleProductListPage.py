from tests.testbase import *

priceValue = str
nameValue = str


class ProductListPage:
    def __init__(self, driver: WebDriver, locators: Locators):
        self.web = driver
        self.get = locators
        self.item = lambda: self.get.byClasses('inventory_item')
        self.itemPrice = lambda: self.get.byClasses('inventory_item_price')
        self.itemName = lambda: self.get.byClasses('inventory_item_name')
        self.itemDesc = lambda: self.get.byClasses('inventory_item_desc')
        self.addToCartButton = lambda: self.get.contains('Add to cart')
        self.removeButton = lambda: self.get.contains('Remove')
        self.shoppingCartIcon = lambda: self.get.byClass('shopping_cart_link')

    def addItemToCart(self, itemIndex: int) -> tuple[priceValue, nameValue]:
        priceValue = self.itemPrice()[itemIndex].text
        print('----- Item to be Added ----')
        print(priceValue)
        nameValue = self.itemName()[itemIndex].text
        print(nameValue)
        self.addToCartButton()[itemIndex].click()
        return priceValue, nameValue

    def gotoShoppingCart(self):
        self.shoppingCartIcon().click()
