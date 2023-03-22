import os

"""Class provides a representation of the product list page of the Sauce Demo application, 
    which is used to interact with the various elements on the page."""


class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("//span[@class='title']")
        self._burger_menu = page.locator("//*[@id='react-burger-menu-btn']")
        self._logout_btn = page.locator("//*[@id='logout_sidebar_link']")
        self._add_to_cart = page.locator("//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self._remove_from_cart = page.locator("//*[@id='remove-sauce-labs-bolt-t-shirt']")
        self._cart_badge = page.locator("//span[@class='shopping_cart_badge']")
        self._cart = page.locator("//a[@class='shopping_cart_link']")

    @property
    def product_header(self):
        return self._products_header

    """Method is used to click the burger menu icon"""
    def click_burger_menu(self):
        return self._burger_menu.click()
    """Method is used to click the logout button"""
    def click_logout(self):
        return self._logout_btn.click()

    def do_logout(self):
        self.click_burger_menu()
        self.click_logout()

    def get_add_cart_locator(self):
        return self._add_to_cart

    """Method is used to click the add to cart button"""
    def click_add_to_cart(self):
        self.get_add_cart_locator().click()
        return self

    def get_remove_from_cart_locator(self):
        return self._remove_from_cart

    """Method is used to click the remove from cart button"""
    def click_remove_from_cart(self):
        self.get_remove_from_cart_locator().click()
        return self

    @property
    def cart_badge(self):
        return self._cart_badge

    """method is used to click the cart link."""
    def click_cart(self):
        self._cart.click()

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it 
        already exists."""
    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
