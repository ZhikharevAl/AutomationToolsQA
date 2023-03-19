class CartPage:
    def __init__(self, page):
        self.page = page
        self._cart_header = page.locator("span[class='title']")
        self._inventory_item_price = page.locator("div[class$='price']")
        self._remove_items = page.locator("button[id='remove-sauce-labs-bolt-t-shirt']")

    def cart_header(self):
        return self._cart_header

    def inventory_item_price(self):
        return self._inventory_item_price

    def get_remove_items_locator(self):
        return self._remove_items

    def click_remove_item(self):
        self.get_remove_items_locator().click()
        return self

