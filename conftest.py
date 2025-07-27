import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session')
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield


@pytest.fixture()
def open_duckduckgo(setup_browser):
    browser.open('https://duckduckgo.com/')
    yield