from ..pages.AuthPage import AuthPage
from ..pages.Schedule import Schedule
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("test.tst345@skyeng.ru","2DbhAAPG6q")

    assert auth_page.get_current_url().endswith("teacher.skyeng.ru/")

def test_create_event(browser):
    schedule_page = Schedule(browser)
    schedule_page.schedule_go()

    assert schedule_page.get_current_url().endswith("skyeng.ru/schedule")

    sleep(10)
