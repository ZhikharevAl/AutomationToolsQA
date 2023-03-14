from playwright.sync_api import Page, expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text('Products')


def test_login_with_invalid_user(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'nonstandard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    expected_fail_massage = 'Username and password do not match any user in this service'
    expect(login_p.error_msg_locator).to_contain_text(expected_fail_massage)


def test_login_no_user_name(setup_teardown) -> None:

    page = setup_teardown
    login_p = LoginPage(page)
    login_p.click_login()
    expected_fail_massage = 'Username is required'
    expect(login_p.error_msg_locator).to_contain_text(expected_fail_massage)


def test_login_no_password(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': ''}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    expected_fail_massage = 'Password is required'
    expect(login_p.error_message_password).to_contain_text(expected_fail_massage)
