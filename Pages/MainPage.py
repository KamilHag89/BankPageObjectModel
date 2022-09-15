from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, url):
        self.address = url
        self.driver = driver
        self.map = MainPageLoc(driver)

    def mainOpen(self):
        self.driver.get(self.address)


class MainPageLoc:
    def __init__(self, driver):
        self.driver = driver

    def returnElement(self, method, target):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((method, target)))

    @property
    def userName(self):
        return self.returnElement(By.NAME, "username")

    @property
    def password(self):
        return self.returnElement(By.NAME, "password")

    @property
    def logInBtn(self):
        return self.returnElement(By.CLASS_NAME, "button")

    @property
    def register(self):
        return self.returnElement(By.LINK_TEXT, "Register")

