from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config import base_url
import allure

@allure.feature("Authentication Tests")
class AuthPage:
    def __init__(self, driver)->None:
        self.__driver = driver
        self.__url = base_url

    def go(self):
        with allure.step('передача url в браузер'):
            self. __driver.get(self.__url)

    def login_as(self, email: str,password: str ):
        with allure.step("Ожидание кликабельности 'войти по паролю' и нажатие на кнопку"):
            element = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.link.link--primary.js-send-otp-form-to-username-password'))
            )
            element.click()
        with allure.step('ввод логина'):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[name="username"][type="text"].input.js-username-password-form-input[placeholder="Телефон, почта или логин"]').send_keys(email)
        with allure.step('Ввод пароля'):
            self.__driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password'].input.js-username-password-form-input.js-username-password-form-password-input[placeholder='Пароль']").send_keys(password)
        with allure.step('нажатие на кнопку войти'):
            self.__driver.find_element(By.CSS_SELECTOR, ".js-username-password-form-button").click()

    def get_current_url(self):
        with allure.step('получение url местонахождения'):
            WebDriverWait(self.__driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title"))
            )
            return self.__driver.current_url