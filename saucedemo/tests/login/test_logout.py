from playwright.sync_api import Page, expect


def xtest_unlogin(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()
    burger_menu = page.locator("//*[@id='react-burger-menu-btn']")
    burger_menu.click()
    logout = page.locator("//*[@id='logout_sidebar_link']")
    logout.click()
    login_logo = page.locator("//div[@class='login_logo']")
    expect(login_logo).to_have_text('Swag Labs')
    user_name = page.locator("//*[@id='user-name']")
    expect(user_name).to_have_text('')
