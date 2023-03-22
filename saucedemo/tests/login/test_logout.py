from playwright.sync_api import expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_unlogin(setup_teardown) -> None:
    """
    The test is checks if a user can successfully log out of a web application and return to the login page.
    """
    page = setup_teardown

    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    products_p.do_logout()

    expect(login_p.login_button).to_be_visible()

    products_p.take_screenshot('test_unlogin.png')
