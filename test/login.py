from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.login_page import LoginPage


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        login = LoginPage(driver)
        login.sign_btn()
        login.enter_email("selim.qups@gmail.com")
        login.enter_password("SelimQups2")
        login.sign_btn()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

