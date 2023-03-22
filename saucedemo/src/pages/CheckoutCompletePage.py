import os

"""This class represents the checkout complete page of an e-commerce website."""


class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self._checkout_complete = page.locator("//*[text() = 'Checkout: Complete!']")

    """Returns the element locator for the checkout header."""

    def checkout_complete_title(self):
        return self._checkout_complete

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it
    already exists."""

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
