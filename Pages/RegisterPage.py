from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class RegisterPage(MainPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def openRegisterForm(self):
        self.mainOpen()
        self.map.register.click()

    @property
    def nameInput(self):
        return self.map.returnElement(By.ID, "customer.firstName")

    @property
    def lastNameInput(self):
        return self.map.returnElement(By.ID, "customer.lastName")

    @property
    def adressInput(self):
        return self.map.returnElement(By.ID, "customer.address.street")

    @property
    def cityInput(self):
        return self.map.returnElement(By.ID, "customer.address.city")

    @property
    def stateInput(self):
        return self.map.returnElement(By.ID, "customer.address.state")

    @property
    def zipInput(self):
        return self.map.returnElement(By.ID, "customer.address.zipCode")

    @property
    def phoneInput(self):
        return self.map.returnElement(By.ID, "customer.phoneNumber")

    @property
    def ssnInput(self):
        return self.map.returnElement(By.ID, "customer.ssn")

    @property
    def usernameInput(self):
        return self.map.returnElement(By.ID, "customer.username")

    @property
    def passwordInput(self):
        return self.map.returnElement(By.ID, "customer.password")

    @property
    def passwordConfiramtionInput(self):
        return self.map.returnElement(By.ID, "repeatedPassword")

    @property
    def registerBtn(self):
        return self.map.returnElement(By.CSS_SELECTOR, "input[value='Register']")
