class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("//span[@class='title']")
        self._burger_menu = page.locator("//*[@id='react-burger-menu-btn']")
        self._logout_btn = page.locator("//*[@id='logout_sidebar_link']")
        self._add_to_cart = page.locator("//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self._remove_from_cart = page.locator("//*[@id='remove-sauce-labs-bolt-t-shirt']")
        self._cart_badge = page.locator("//span[@class='shopping_cart_badge']")

    @property
    def product_header(self):
        """ It returns locator or selector for product header text """
        return self._products_header

    def click_burger_menu(self):
        """ Click on the Burger menu icon in the header """
        return self._burger_menu.click()

    def click_logout(self):
        """ This will click on logout """
        return self._logout_btn.click()

    def do_logout(self):
        """ Logout from the sauce demo"""
        self.click_burger_menu()
        self.click_logout()

    def get_add_cart_locator(self):
        """This will return locator of Add to cart button or Remove button"""
        return self._add_to_cart

    def click_add_to_cart(self):
        self.get_add_cart_locator().click()
        return self

    def get_remove_from_cart_locator(self):
        return self._remove_from_cart

    def click_remove_from_cart(self):
        self.get_remove_from_cart_locator().click()
        return self



    @property
    def cart_badge(self):
        return self._cart_badge


