import logging
import pytest


@pytest.fixture()
def setup_teardown(page) -> None:
    page.set_viewport_size({'width': 1536, 'height': 800})
    page.goto("https://www.saucedemo.com")
    yield page


def pytest_configure():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pytest_runtest_logreport(report):
    if report.when == "setup" and logging.getLogger().isEnabledFor(logging.INFO):
        logging.info("Test run: %s", report.nodeid)
    elif report.when == "teardown" and logging.getLogger().isEnabledFor(logging.INFO):
        logging.info("Test completion: %s", report.nodeid)

