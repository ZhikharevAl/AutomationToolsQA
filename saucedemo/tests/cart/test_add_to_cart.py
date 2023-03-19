from playwright.sync_api import expect

from saucedemo.src.pages.CartPage import CartPage
from saucedemo.src.pages.LoginPage import LoginPage


def test_place_order(setup_teardown) -> None:
    """
    
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    expect(cart_p._cart_header).to_have_text("Your Cart")
    expect(cart_p._inventory_item_price).to_have_text("$15.99")


def test_remove_item_from_cart(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    cart_p.click_remove_item()

    expect(cart_p._cart_header).to_have_text("Your Cart")
    expect(products_p.cart_badge).not_to_be_visible()


def test_continue_shopping(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    cart_p.click_continue_shopping()

    expect(products_p.product_header).to_have_text('Products')
