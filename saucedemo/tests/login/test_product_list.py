from playwright.sync_api import expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_add_to_cart(setup_teardown) -> None:
    """
    Method of adding product to shopping cart.
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()

    expect(products_p.cart_badge).to_have_text("1")


def test_remove_product_cart(setup_teardown) -> None:
    """
    Method of removing an item from the cart.
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_remove_from_cart()

    expect(products_p.cart_badge).not_to_be_visible()




