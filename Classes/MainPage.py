from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.Locators import mainUrl


class MainPage:
    def __init__(self, driver):
        self.address = mainUrl
        self.driver = driver
        self.map = MainPageLoc(driver)

    def mainOpen(self):
        self.driver.get(self.address)


class MainPageLoc:
    def __init__(self, driver):
        self.driver = driver

    @property
    def userName(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    @property
    def password(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    @property
    def logInBtn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button")))
