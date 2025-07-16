import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene.support.shared import browser as selene_browser

@pytest.fixture(scope='session')
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(200, 300)
    selene_browser.config.driver = driver  # связываем Selene с нашим драйвером
    yield driver
    driver.quit()

@pytest.fixture()
def opening_browser(driver):
    driver.get('https://duckduckgo.com/')