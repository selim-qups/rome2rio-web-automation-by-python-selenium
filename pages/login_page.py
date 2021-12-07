import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import *


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.signin_btn_xpath = SigninLocator.signin_btn_xpath
        self.email_input_id = SigninLocator.email_input_id
        self.password_input_id = SigninLocator.password_input_id
        self.submit_btn_id = SigninLocator.submit_btn_id

    def sign_btn(self):
        self.driver.find_element(By.XPATH, SigninLocator.signin_btn_xpath).click()
        time.sleep(1)

    def enter_email(self, email):
        self.driver.find_element(By.ID, SigninLocator.email_input_id).send_keys(email)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, SigninLocator.password_input_id).send_keys(password)
        time.sleep(1)

    def sign_submit_btn(self):
        self.driver.find_element(By.ID, SigninLocator.submit_btn_id)
        time.sleep(1)