class CheckoutYourInformationPage:
    def __init__(self, page):
        self.page = page
        self._checkout_header = page.locator("span[class='title']")
        self._first_name = page.locator("input[id='first-name']")
        self._last_name = page.locator("input[id='last-name']")
        self._zipcode = page.locator("input[id='postal-code']")

    def checkout_header(self):
        return self._checkout_header

    def first_name_locator(self):
        return self._first_name

    def add_first_name(self):
        self.first_name_locator().fill("John")
        return self

    def last_name_locator(self):
        return self._last_name

    def add_last_name(self):
        self.last_name_locator().fill("Snow")
        return self

    def zipcode_locator(self):
        return self._zipcode

    def add_zipcode(self):
        self.zipcode_locator().fill("458769")
        return self

