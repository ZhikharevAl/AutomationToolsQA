from playwright.sync_api import Page, expect


def test_login_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    products_header = page.locator("//span[@class='title']")

    expect(products_header).to_have_text('Products')

