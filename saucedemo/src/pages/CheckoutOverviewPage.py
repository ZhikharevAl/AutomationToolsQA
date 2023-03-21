import os


class CheckoutOverviewPage:

    def __init__(self, page):
        self.page = page
        self._checkout_overview = page.locator("//*[text() = 'Checkout: Overview']")
        self._finish = page.locator("button[id='finish']")

    def checkout_overview(self):
        return self._checkout_overview

    def finish_locator(self):
        return self._finish

    def click_finish(self):
        self.finish_locator().click()
        return self

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
