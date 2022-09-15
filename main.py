from Data.drivers import chrome
from Pages.MainPage import MainPage
from Pages.RegisterPage import RegisterPage
from Data.Locators import mainUrl
from Data.TestUser import User


user = User()
test = RegisterPage(chrome, mainUrl)
test.openRegisterForm()
test.nameInput.send_keys(user.name)
test.lastNameInput.send_keys(user.lastname)
test.adressInput.send_keys(user.adress)
test.registerBtn.click()
