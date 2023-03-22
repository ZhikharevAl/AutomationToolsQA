import os

"""This class represents the checkout overview page of an e-commerce website"""


class CheckoutOverviewPage:

    def __init__(self, page):
        self.page = page
        self._checkout_overview = page.locator("//*[text() = 'Checkout: Overview']")
        self._finish = page.locator("button[id='finish']")

    """Returns the element locator for the checkout overview page header."""

    def checkout_overview(self):
        return self._checkout_overview

    """returns the element locator for the "Finish" button."""

    def finish_locator(self):
        return self._finish

    """Clicks on the "Finish" button."""

    def click_finish(self):
        self.finish_locator().click()
        return self

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it 
        already exists."""

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
