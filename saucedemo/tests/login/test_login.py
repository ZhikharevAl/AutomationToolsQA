from playwright.sync_api import Page, expect


def test_login_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    products_header = page.locator("//span[@class='title']")

    expect(products_header).to_have_text('Products')


def test_unlogin(page: Page) -> None:
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


def test_login_with_invalid_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    expected_fail_massage = 'Username and password do not match any user in this service'
    error_msg_locator = page.locator("//h3")
    expect(error_msg_locator).to_contain_text(expected_fail_massage)


def test_login_no_user_name(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("")
    page.get_by_text("Login").click()

    expected_fail_massage = 'Username is required'
    error_msg_locator = page.locator("//h3")
    expect(error_msg_locator).to_contain_text(expected_fail_massage)


def test_login_no_password(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("")
    page.get_by_text("Login").click()

    expected_fail_massage = 'Password is required'
    error_msg_locator = page.locator("//h3")
    expect(error_msg_locator).to_contain_text(expected_fail_massage)
