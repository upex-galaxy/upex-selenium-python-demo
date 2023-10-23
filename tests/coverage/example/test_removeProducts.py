from random import randint
import pytest
from tests.testbase import *


class TestRemoveProducts:

    # * TC1: (No POM) Validate adding and removing one Product, the shoppingCart should be empty
    def test_removeProduct(self, loginSuccessful: Test):
        web, get = loginSuccessful

        items = get.contains('Add to cart')
        option = randint(0, 5)  # Should be 5 elements

        addToCartButton = items[option]

        addToCartButton.click()

        get.byClass('shopping_cart_link').click()
        expect(web.current_url).toContain('cart.html')

        def cartItems(): return get.byClasses('cart_quantity')

        itemsBeforeRemove = len(cartItems())
        expect(itemsBeforeRemove).toBeEqual(1)

        removeButton = get.bySelector('[data-test*="remove"]')
        removeButton.click()

        itemsAfterRemove = len(cartItems())
        expect(itemsAfterRemove).toBeEqual(0)
