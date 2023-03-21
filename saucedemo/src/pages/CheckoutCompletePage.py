class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self._checkout_complete = page.locator("//*[text() = 'Checkout: Complete!']")

    def checkout_complete_title(self):
        return self._checkout_complete
