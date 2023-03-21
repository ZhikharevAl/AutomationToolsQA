import os


class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self._checkout_complete = page.locator("//*[text() = 'Checkout: Complete!']")

    def checkout_complete_title(self):
        return self._checkout_complete

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
