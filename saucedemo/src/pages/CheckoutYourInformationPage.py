class CheckoutYourInformationPage:
    def __init__(self, page):
        self.page = page
        self._checkout_header = page.locator("span[class='title']")

    def checkout_header(self):
        return self._checkout_header
