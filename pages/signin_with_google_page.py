import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.locators import *


class SigninWithGoogle():

    def __init__(self, driver):
        self.driver = driver

        self.signinBtnXpath = SigninWithGoogleLocators.signinBtnXpath
        self.googleBtnId = SigninWithGoogleLocators.googleBtnId
        self.email = SigninWithGoogleLocators.emailX
        self.nextBtn = SigninWithGoogleLocators.nextbtnX
        self.password = SigninWithGoogleLocators.passX
        self.submit = SigninWithGoogleLocators.subbtnX

    def signin_btn(self):
        self.driver.find_element(By.XPATH, SigninWithGoogleLocators.signinBtnXpath).click()
        time.sleep(1)

    def google_btn(self):
        self.driver.find_element(By.ID, SigninWithGoogleLocators.googleBtnId).click()
        time.sleep(1)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, SigninWithGoogleLocators.emailX).send_keys(email)
        time.sleep(2)

    def nex_btn(self):
        self.driver.find_element(By.XPATH, SigninWithGoogleLocators.nextbtnX).click()

    def enter_pass(self, password):
        self.driver.find_element(By.NAME, SigninWithGoogleLocators.passX).send_keys(password)
        time.sleep(5)

    def submit_btn(self):
        self.driver.find_element(By.XPATH, SigninWithGoogleLocators.subbtnX).click()