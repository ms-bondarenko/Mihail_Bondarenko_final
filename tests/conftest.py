import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser

    browser.quit()