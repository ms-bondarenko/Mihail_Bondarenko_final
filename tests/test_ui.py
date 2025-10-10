from .conftest import browser
from ..pages.AuthPage import AuthPage
from ..pages.Schedule import Schedule
from time import sleep
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
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "long-view__time")))

    assert element is not None
def test_title_page(browser):
    schedule_page = Schedule(browser)
    title = schedule_page.title_page()

    assert title == "Расписание"
