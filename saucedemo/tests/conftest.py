import pytest


@pytest.fixture()
def setup_teardown(page) -> None:
    page.set_viewport_size({'width': 1536, 'height': 800})
    page.goto("https://www.saucedemo.com")
    yield page
