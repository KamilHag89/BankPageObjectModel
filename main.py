from Data.drivers import chrome
from Classes.MainPage import MainPage

test = MainPage(chrome)
test.mainOpen()
test.map.userName.send_keys("asddas")
test.map.password.send_keys("asdasd")
test.map.logInBtn.click()
