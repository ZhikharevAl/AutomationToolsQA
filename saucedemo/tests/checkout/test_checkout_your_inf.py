from playwright.sync_api import expect

from saucedemo.src.pages.CartPage import CartPage
from saucedemo.src.pages.CheckoutOverviewPage import CheckoutOverviewPage
from saucedemo.src.pages.CheckoutYourInformationPage import CheckoutYourInformationPage
from saucedemo.src.pages.LoginPage import LoginPage


def test_checkout_your_inf(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()
    cart_p = CartPage(page)
    cart_p.click_checkout()
    checkout_p = CheckoutYourInformationPage(page)

    checkout_p.add_first_name()
    checkout_p.add_last_name()
    checkout_p.add_zipcode()

    checkout_p.click_continue()

    checkout_o = CheckoutOverviewPage(page)

    expect(checkout_o.checkout_overview()).to_have_text("Checkout: Overview")

    checkout_o.take_screenshot('test_checkout_your_inf.png')
