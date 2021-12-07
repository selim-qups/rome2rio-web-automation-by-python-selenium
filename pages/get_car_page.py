import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import GetCarLocators


class GetCarPage():
    def __init__(self, driver):
        self.driver = driver

        self.carBtn = GetCarLocators.carBtnId
        self.fromId = GetCarLocators.carsfromId
        self.pickupdate = GetCarLocators.carsearchId

    def car_btn(self):
        self.driver.find_element(By.ID, GetCarLocators.carBtnId).click()
        time.sleep(2)

    def car_from(self, from_location):
        self.driver.find_element(By.ID, GetCarLocators.carsfromId).send_keys(from_location)

    def pickup_date(self):
        self.driver.find_element(By.ID, GetCarLocators.carsearchId).click()
        time.sleep(2)