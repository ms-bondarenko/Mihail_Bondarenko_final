from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Schedule:
    def __init__(self, driver)->None:
        self.__driver = driver

    def schedule_go(self):
        go = self.__driver.find_element(By.XPATH, "//div[contains(text(), 'Расписание')]").click()

    def get_current_url(self):
        WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "month"))
        )
        return self.__driver.current_url