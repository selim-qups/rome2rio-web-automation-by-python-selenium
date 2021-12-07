from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.signup_page import SignupPage


class SignupTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_signup(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        signup = SignupPage(driver)
        signup.sign_btn()
        signup.signup_btn()
        signup.enter_email("selim.qups@gmail.com")
        signup.enter_name("Selim reza")
        signup.enter_password("SelimQups2")
        signup.enter_re_password("SelimQups2")
        signup.sign_up_submit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

