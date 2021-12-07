from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.signin_with_google_page import SigninWithGoogle


class SignupWithGoogleTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_signup(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        signup = SigninWithGoogle(driver)

        signup.signin_btn()
        signup.google_btn()
        driver.get("https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fwww.rome2rio.com%2Fgoogle-sign-in&response_type=permission id_token&scope=email profile openid&openid.realm&include_granted_scopes=true&client_id=736771455123-ttjjkfnroislf3r41m0ct2hhc1f8deh1.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fwww.rome2rio.com&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow")
        signup.enter_email("selim.qups@gmail.com")
        signup.nex_btn()
        signup.enter_pass("SelimQups2")
        signup.submit_btn()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)






if __name__ == '__main__':
    unittest.main()

