
class CheckoutOverviewPage:

    def __init__(self, page):
        self.page = page
        self._checkout_overview = page.locator("//*[text() = 'Checkout: Overview']")

    def checkout_overview(self):
        return self._checkout_overview
