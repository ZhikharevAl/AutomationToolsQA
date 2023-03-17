from playwright.sync_api import expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_add_to_cart(setup_teardown) -> None:
    """
    Verify that add to cart button is changed to Remove when clicked
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart_or_remove()

    expect(products_p.cart_badge).to_have_text("1")


