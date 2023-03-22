import os

"""This class represents the cart page of an e-commerce website."""


class CartPage:
    def __init__(self, page):
        self.page = page
        self._cart_header = page.locator("span[class='title']")
        self._inventory_item_price = page.locator("div[class$='price']")
        self._remove_items = page.locator("button[id='remove-sauce-labs-bolt-t-shirt']")
        self._continue_shopping = page.locator("button[id='continue-shopping']")
        self._checkout = page.locator("button[id='checkout']")

    """Returns the element locator for the cart header."""

    def cart_header(self):
        return self._cart_header

    """Returns the element locator for the item prices in the cart."""

    def inventory_item_price(self):
        return self._inventory_item_price

    """Returns the element locator for the "remove" button of the first item in the cart."""

    def get_remove_items_locator(self):
        return self._remove_items

    """ Clicks the "remove" button of the first item in the cart."""

    def click_remove_item(self):
        self.get_remove_items_locator().click()
        return self

    """Returns the element locator for the "continue shopping" button on the cart page."""

    def get_continue_shopping_locator(self):
        return self._continue_shopping

    """Clicks the "continue shopping" button on the cart page."""

    def click_continue_shopping(self):
        self.get_continue_shopping_locator().click()
        return self

    """Returns the element locator for the "checkout" button on the cart page."""

    def get_checkout_locator(self):
        return self._checkout

    """Clicks the "checkout" button on the cart page."""

    def click_checkout(self):
        self.get_checkout_locator().click()
        return self

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it 
        already exists."""

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
