from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
        self.__driver.find_element(By.XPATH, '//*[@style="top: 984px; left: 1px; width: 127px; height: 40px;"]').click()
        wait = WebDriverWait(self.__driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Личное событие')]")))
        element.click()

        wait = WebDriverWait(self.__driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")))
        el.click()
        el.send_keys("Дополнительный урок")

        wait = WebDriverWait(self.__driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[rows='5']")))
        el.click()
        el.send_keys("Иванов")

        self.__driver.find_element(By.XPATH, "//*[contains(@style, 'fill: rgb(235, 253, 242);')]").click()
        self.__driver.find_element(By.CSS_SELECTOR, ".root.-type-primary.-color-brand.-size-m.-active").click()


    def editing(self):
        self.__driver.find_element(By.XPATH, '[text()="12:00 – 12:30"]').click()
