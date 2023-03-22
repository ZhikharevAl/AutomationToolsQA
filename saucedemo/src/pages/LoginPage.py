import os

from saucedemo.src.pages.ProductListPage import ProductListPage

"""Class that is responsible for handling actions on the login page of a web application."""


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_message = page.locator("//h3")
        self._error_message_password = page.locator("h3[data-test='error']")

    """Clears the input field for the username and fills in the provided value."""

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)

    """Clears the input field for the password and fills in the provided value."""

    def enter_password(self, p_word):
        self._password.clear()
        self._password.fill(p_word)

    """Clicks the login button."""

    def click_login(self):
        self._login_btn.click()

    """Combines the above methods to enter the provided credentials and click the login button. 
    It returns a ProductListPage object that represents the product list page of the application."""

    def do_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login()
        return ProductListPage(self.page)

    """Returns the element locator for the error message that appears when the user's login credentials are invalid."""

    @property
    def error_msg_locator(self):
        return self._error_message

    """Returns the element locator for the error message that appears when the user's password is invalid."""

    @property
    def error_message_password(self):
        return self._error_message

    """Returns the element locator for the login button."""

    @property
    def login_button(self):
        return self._login_btn

    """Takes a full-page screenshot of the cart page and saves it to the specified file path, overwriting it if it 
        already exists."""

    def take_screenshot(self, filename):
        path = 'C:/Users/1/AquaProjects/AutomationToolsQA/saucedemo/screenshot/' + filename
        if os.path.exists(path):
            os.remove(path)
        self.page.screenshot(path=path, full_page=True)
