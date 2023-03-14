class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("//span[@class='title']")
        self._burger_menu = page.locator("//*[@id='react-burger-menu-btn']")
        self._logout_btn = page.locator("//*[@id='logout_sidebar_link']")

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
