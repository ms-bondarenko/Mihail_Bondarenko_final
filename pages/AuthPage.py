from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config import base_url


class AuthPage:
    def __init__(self, driver)->None:
        self.__driver = driver
        self.__url = base_url

    def go(self):
        self. __driver.get(self.__url)

    def login_as(self, email: str,password: str ):
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.link.link--primary.js-send-otp-form-to-username-password'))
        )
        element.click()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[name="username"][type="text"].input.js-username-password-form-input[placeholder="Телефон, почта или логин"]').send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password'].input.js-username-password-form-input.js-username-password-form-password-input[placeholder='Пароль']").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, ".js-username-password-form-button").click()

    def get_current_url(self):
        WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        return self.__driver.current_url
# class AuthPage:
#     def __init__(self, driver) -> None:
#         self.__driver = driver
#         self.__url = base_url
#
#     @allure.step("Navigating to Auth Page")
#     def go(self):
#         allure.attach(self.__url, name="URL", attachment_type=allure.attachment_type.TEXT)
#         self.__driver.get(self.__url)
#
#     @allure.step("Logging in with email: {email}")
#     def login_as(self, email: str, password: str):
#         try:
#             element = WebDriverWait(self.__driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, '.link.link--primary.js-send-otp-form-to-username-password'))
#             )
#             element.click()
#             allure.attach("Clicked on OTP link", name="OTP Link Clicked", attachment_type=allure.attachment_type.TEXT)
#
#             self.__enter_text(By.CSS_SELECTOR, 'input[name="username"][type="text"]', email)
#             self.__enter_text(By.CSS_SELECTOR, "input[name='password'][type='password']", password)
#
#             button = self.__driver.find_element(By.CSS_SELECTOR, ".js-username-password-form-button")
#             button.click()
#             allure.attach("Clicked on login button", name="Login Button Clicked", attachment_type=allure.attachment_type.TEXT)
#         except Exception as e:
#             allure.attach(str(e), name="Login Error", attachment_type=allure.attachment_type.TEXT)
#             print(f"Error during login: {e}")
#
#     @allure.step("Entering text into input")
#     def __enter_text(self, by, value, text):
#         input_element = WebDriverWait(self.__driver, 10).until(
#             EC.presence_of_element_located((by, value))
#         )
#         allure.attach(f"Entering text: {text}", name="Input Text", attachment_type=allure.attachment_type.TEXT)
#         input_element.send_keys(text)
#
#     @allure.step("Getting current URL")
#     def get_current_url(self):
#         WebDriverWait(self.__driver, 15).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "title"))
#         )
#         current_url = self.__driver.current_url
#         allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
#         return current_url