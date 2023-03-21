from playwright.sync_api import expect

from saucedemo.src.pages.CartPage import CartPage
from saucedemo.src.pages.CheckoutOverviewPage import CheckoutOverviewPage
from saucedemo.src.pages.CheckoutYourInformationPage import CheckoutYourInformationPage
from saucedemo.src.pages.CheckoutCompletePage import CheckoutCompletePage
from saucedemo.src.pages.LoginPage import LoginPage


def test_finish(setup_teardown) -> None:
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
    checkout_c = CheckoutCompletePage(page)
    checkout_o.click_finish()

    expect(checkout_c.checkout_complete_title()).to_have_text("Checkout: Complete!")

    checkout_c.take_screenshot('test_finish.png')