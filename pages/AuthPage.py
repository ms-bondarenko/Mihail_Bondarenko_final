from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver)->None:
        self.__driver = driver
        self.__url = "https://id.skyeng.ru/login"

    def go(self):
        self. __driver.get(self.__url)

    def login_as(self, email: str,password: str ):
        self.__driver.find_element(By.CSS_SELECTOR, '.link.link--primary.js-send-otp-form-to-username-password').click()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[name="username"][type="text"].input.js-username-password-form-input[placeholder="Телефон, почта или логин"]').send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password'].input.js-username-password-form-input.js-username-password-form-password-input[placeholder='Пароль']").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, ".js-username-password-form-button").click()

    def get_current_url(self):
        WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        return self.__driver.current_url