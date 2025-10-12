from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Schedule:
    def __init__(self, driver)->None:
        self.__driver = driver

    def schedule_go(self):
        self.__driver.find_element(By.XPATH, "//div[contains(text(), 'Расписание')]").click()

    def get_current_url(self):
        WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "month"))
        )
        return self.__driver.current_url

    def create(self):
        add_icon = self.__driver.find_element(By.CSS_SELECTOR, "ds-icon.add-icon.-size-m")
        add_icon.click()
        wait = WebDriverWait(self.__driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Личное событие')]")))
        element.click()

    def input_title(self):
        wait = WebDriverWait(self.__driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")))
        el.click()
        el.send_keys("Дополнительный урок")

    def input_description(self):
        wait = WebDriverWait(self.__driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[rows='5']")))
        el.click()
        el.send_keys("Иванов")

        self.__driver.find_element(By.XPATH, "//*[contains(@style, 'fill: rgb(235, 253, 242);')]").click()
        self.__driver.find_element(By.CSS_SELECTOR, ".root.-type-primary.-color-brand.-size-m.-active").click()


    def title_page(self):
        self.__driver.get("https://teachers.skyeng.ru/schedule")
        wait = WebDriverWait(self.__driver, 10)  # ждем до 10 секунд
        title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-title.mr16')))
        return title.text

    def delite(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']"))
        )
        element.click()

        button = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'root') and .//div[text()=' Удалить ']]"))
        )
        button.click()

# class Schedule:
#     def __init__(self, driver) -> None:
#         self.__driver = driver
#
#     @allure.step("Navigating to the Schedule page")
#     def schedule_go(self):
#         allure.attach("Clicked on schedule link", name="Schedule Navigation",
#                       attachment_type=allure.attachment_type.TEXT)
#         self.__driver.find_element(By.XPATH, "//div[contains(text(), 'Расписание')]").click()
#
#     @allure.step("Getting current URL")
#     def get_current_url(self):
#         WebDriverWait(self.__driver, 15).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "month"))
#         )
#         current_url = self.__driver.current_url
#         allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
#         return current_url
#
#     @allure.step("Creating a new event")
#     def create(self):
#         add_icon = self.__driver.find_element(By.CSS_SELECTOR, "ds-icon.add-icon.-size-m")
#         add_icon.click()
#         allure.attach("Clicked on Add Event icon", name="Add Event", attachment_type=allure.attachment_type.TEXT)
#
#         wait = WebDriverWait(self.__driver, 10)
#         element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Личное событие')]")))
#         element.click()
#         allure.attach("Clicked on Personal Event option", name="Event Type",
#                       attachment_type=allure.attachment_type.TEXT)
#
#     @allure.step("Inputting title for the new event")
#     def input_title(self):
#         wait = WebDriverWait(self.__driver, 10)
#         el = wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")))
#         el.click()
#         el.send_keys("Дополнительный урок")
#         allure.attach("Entered title: Дополнительный урок", name="Title Input",
#                       attachment_type=allure.attachment_type.TEXT)
#
#     @allure.step("Inputting description for the new event")
#     def input_description(self):
#         wait = WebDriverWait(self.__driver, 10)
#         el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[rows='5']")))
#         el.click()
#         el.send_keys("Иванов")
#         allure.attach("Entered description: Иванов", name="Description Input",
#                       attachment_type=allure.attachment_type.TEXT)
#
#         self.__driver.find_element(By.XPATH, "//*[contains(@style, 'fill: rgb(235, 253, 242);')]").click()
#         self.__driver.find_element(By.CSS_SELECTOR, ".root.-type-primary.-color-brand.-size-m.-active").click()
#         allure.attach("Clicked on Save Event button", name="Save Event", attachment_type=allure.attachment_type.TEXT)
#
#     @allure.step("Getting the title of the page")
#     def title_page(self):
#         self.__driver.get("https://teachers.skyeng.ru/schedule")
#         wait = WebDriverWait(self.__driver, 10)
#         title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-title.mr16')))
#         allure.attach(title.text, name="Page Title", attachment_type=allure.attachment_type.TEXT)
#         return title.text
#
#     @allure.step("Deleting an event")
#     def delite(self):
#         element = WebDriverWait(self.__driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//div[@class='long-view__title' and text()='Дополнительный урок']"))
#         )
#         element.click()
#         allure.attach("Clicked on event to delete", name="Delete Event Click",
#                       attachment_type=allure.attachment_type.TEXT)
#
#         button = WebDriverWait(self.__driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'root') and .//div[text()=' Удалить ']]"))
#         )
#         button.click()
#         allure.attach("Clicked on Delete button", name="Confirm Delete", attachment_type=allure.attachment_type.TEXT)
#
#
