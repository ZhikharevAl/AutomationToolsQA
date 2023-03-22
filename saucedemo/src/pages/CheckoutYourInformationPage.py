import os
import random
import string

first_name = ''.join(random.choices(string.ascii_letters, k=6)).capitalize()
last_name = ''.join(random.choices(string.ascii_letters, k=10)).capitalize()

"""This is a class representing the "Checkout: Your Information" page of an e-commerce website."""


class CheckoutYourInformationPage:
    def __init__(self, page):
        self.page = page
        self._checkout_header = page.locator("span[class='title']")
        self._first_name = page.locator("input[id='first-name']")
        self._last_name = page.locator("input[id='last-name']")
        self._zipcode = page.locator("input[id='postal-code']")
        self._continue = page.locator("input[id='continue']")

    """Returns the element locator for the checkout header."""
    def checkout_header(self):
        return self._checkout_header

    """Returns the element locator for the first name field."""
    def first_name_locator(self):
        return self._first_name

    """Fills in a random first name generated using the random and string modules."""
    def add_first_name(self):
        self.first_name_locator().fill(first_name)
        return self

    """Returns the element locator for the last name field."""
    def last_name_locator(self):
        return self._last_name

    """Fills in a random last name generated using the random and string modules."""
    def add_last_name(self):
        self.last_name_locator().fill(last_name)
        return self

    """Returns the element locator for the zip code field."""
    def zipcode_locator(self):
        return self._zipcode

    """Fills in a random zip code using the random module."""
    def add_zipcode(self):
        self.zipcode_locator().fill(str(random.randint(100000, 999999)))
        return self

    """Returns the element locator for the continue button."""
    def continue_locator(self):
        return self._continue

    """Clicks the continue button."""
    def click_continue(self):
        self.continue_locator().click()
        return self

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it 
        already exists."""
    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
