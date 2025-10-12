from .conftest import browser
from pages.AuthPage import AuthPage
from ..pages.Schedule import Schedule
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import login , password
import allure

@allure.story('переход на страницу авторизации , ввод логина и пароля,логинизация')
def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(login,password)
    with allure.step('проверка полученного url на соответствие url страницы преподавателей'):
        assert auth_page.get_current_url().endswith("teacher.skyeng.ru/")

@allure.story('создание личного события')
def test_create_event(browser):
    schedule_page = Schedule(browser)
    with allure.step('переход в расписание'):
        schedule_page.schedule_go()

    assert schedule_page.get_current_url().endswith("skyeng.ru/schedule")

def test_title_page(browser):
    schedule_page = Schedule(browser)
    with allure.step('проверка нахождения на странице расписание'):
        title = schedule_page.title_page()

    assert title == "Расписание"

    schedule_page.create()

def test_input_title(browser):
    with allure.step('заполнение наименования события'):
        schedule_page = Schedule(browser)
        schedule_page.input_title()
    with allure.step('проверка что в поле наименование отображается кол-во введенных символов'):
        simbols = browser.find_element(By.CSS_SELECTOR, ".limit-hint__title-hint.text-body-normal").text
        assert simbols == "19 / 40 символов"

def test_input_description(browser):
    with allure.step('заполнение описания , присвоение цвета и сохранение события'):
        schedule_page = Schedule(browser)
        schedule_page.input_description()

    with allure.step('ожидание появления события и проверка что элемент события не соответствует None'):
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']")))
        assert element is not None
@allure.story('Удаление события')
def test_delite_event(browser):
    schedule_page = Schedule(browser)
    with allure.step('удаление ранее нами созданного события'):
        schedule_page.delite()
    with allure.step('ожидание загрузки событий и проверка что утверждение присутствия элемента на странице ,ложно '):
        WebDriverWait(browser, 10).until_not(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']"))
        )
        assert True

