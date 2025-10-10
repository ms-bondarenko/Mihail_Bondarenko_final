from .conftest import browser
from ..pages.AuthPage import AuthPage
from ..pages.Schedule import Schedule
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..tests.config import login , password

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(login,password)

    assert auth_page.get_current_url().endswith("teacher.skyeng.ru/")

def test_create_event(browser):
    schedule_page = Schedule(browser)
    schedule_page.schedule_go()

    assert schedule_page.get_current_url().endswith("skyeng.ru/schedule")

    schedule_page.create()

def test_input_title(browser):
    schedule_page = Schedule(browser)
    schedule_page.input_title()

def test_input_description(browser):
    schedule_page = Schedule(browser)
    schedule_page.input_description()

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']")))
    assert element is not None

def test_title_page(browser):
    schedule_page = Schedule(browser)
    title = schedule_page.title_page()

    assert title == "Расписание"

def test_delite_event(browser):
    schedule_page = Schedule(browser)
    schedule_page.delite()
    WebDriverWait(browser, 10).until_not(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']"))
    )
    assert True

