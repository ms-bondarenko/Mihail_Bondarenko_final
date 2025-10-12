from .conftest import browser
from pages.AuthPage import AuthPage
from ..pages.Schedule import Schedule
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import login , password


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

    simbols = browser.find_element(By.CSS_SELECTOR, ".limit-hint__title-hint.text-body-normal").text
    assert simbols == "19 / 40 символов"

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

# @allure.story("Authentication")
# def test_auth(browser):
#     auth_page = AuthPage(browser)
#     auth_page.go()
#     auth_page.login_as(login, password)
#
#     current_url = auth_page.get_current_url()
#     allure.attach(current_url, name="Current URL after login", attachment_type=allure.attachment_type.TEXT)
#     assert current_url.endswith("teacher.skyeng.ru/")
#
# @allure.story("Schedule Management")
# def test_create_event(browser):
#     schedule_page = Schedule(browser)
#     schedule_page.schedule_go()
#
#     current_url = schedule_page.get_current_url()
#     allure.attach(current_url, name="Current URL after navigating to schedule", attachment_type=allure.attachment_type.TEXT)
#     assert current_url.endswith("skyeng.ru/schedule")
#
#     schedule_page.create()
#
# @allure.story("Input Title")
# def test_input_title(browser):
#     schedule_page = Schedule(browser)
#     schedule_page.input_title()
#
# @allure.story("Input Description")
# def test_input_description(browser):
#     schedule_page = Schedule(browser)
#     schedule_page.input_description()
#
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']"))
#     )
#     allure.attach("Element found", name="Input Description Result", attachment_type=allure.attachment_type.TEXT)
#     assert element is not None
#
# @allure.story("Title Verification")
# def test_title_page(browser):
#     schedule_page = Schedule(browser)
#     title = schedule_page.title_page()
#
#     allure.attach(title, name="Current Title", attachment_type=allure.attachment_type.TEXT)
#     assert title == "Расписание"
#
# @allure.story("Delete Event")
# def test_delite_event(browser):
#     schedule_page = Schedule(browser)
#     schedule_page.delite()
#
#     WebDriverWait(browser, 10).until_not(
#         EC.presence_of_element_located(
#             (By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']")
#         )
#     )
#     allure.attach("Element deleted", name="Delete Event Result", attachment_type=allure.attachment_type.TEXT)
#     assert True

