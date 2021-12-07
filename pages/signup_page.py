import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import *


class SignupPage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_btn_xpath = SignupLocators.signin_btn_xpath
        self.signup_btn_xpath = SignupLocators.signup_btn_xpath
        self.email_inputId = SignupLocators.email_inputId
        self.name_inputId = SignupLocators.name_inputId
        self.pass_inputId = SignupLocators.pass_inputId
        self.repass_inputId = SignupLocators.repass_inputId
        self.signup_sub_btnId = SignupLocators.signup_sub_btnId

    def sign_btn(self):
        self.driver.find_element(By.XPATH, SignupLocators.signin_btn_xpath).click()
        time.sleep(1)

    def signup_btn(self):
        self.driver.find_element(By.XPATH, SignupLocators.signup_btn_xpath).click()
        time.sleep(1)

    def enter_email(self, email):
        self.driver.find_element(By.ID, SignupLocators.email_inputId).send_keys("selim.qups@gmail.com")
        time.sleep(1)

    def enter_name(self, email):
        self.driver.find_element(By.ID, SignupLocators.name_inputId).send_keys("Selim Reza")
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, SignupLocators.pass_inputId).send_keys("SelimQups2")
        time.sleep(1)

    def enter_re_password(self, password):
        self.driver.find_element(By.ID, SignupLocators.repass_inputId).send_keys("SelimQups2")
        time.sleep(1)

    def sign_up_submit(self):
        self.driver.find_element(By.ID, SignupLocators.signup_sub_btnId).click()
        time.sleep(1)