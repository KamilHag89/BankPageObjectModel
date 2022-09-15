from Data.drivers import chrome
from Classes.MainPage import MainPage
from Data.Locators import mainUrl

test = MainPage(chrome, mainUrl)
test.mainOpen()
test.map.userName.send_keys("asddas")
test.map.password.send_keys("asdasd")
test.map.logInBtn.click()
