import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import *


class GetHotelPage():
    def __init__(self, driver):
        self.driver = driver

        self.hotelBtnid = GetHotel.hotelBtnId
        self.hotelLocation = GetHotel.hotellocationXpath
        self.hotelCheckin = GetHotel.checkinDateXpath
        self.hotelDateXpath = GetHotel.checkinDateSelectXpath
        self.serarchBtn = GetHotel.searchBtnId
        self.nextPageXpath = GetHotel.nextPageXpath
        self.ability = GetHotel.see_abilityXpath

    def hotel_btn(self):
        self.driver.find_element(By.ID, GetHotel.hotelBtnId).click()
        time.sleep(1)

    def hotel_location(self, location):
        self.driver.find_element(By.XPATH, GetHotel.hotellocationXpath).send_keys(location)

    def checkin_Hdate(self):
        self.driver.find_element(By.XPATH, GetHotel.checkinDateXpath).click()
        time.sleep(1)

    def checkin_date_select(self):
        self.driver.find_element(By.XPATH, GetHotel.checkinDateSelectXpath).click()
        time.sleep(1)

    def search_btn(self):
        self.driver.find_element(By.ID, GetHotel.searchBtnId).click()
        time.sleep(2)

    def go_next_page(self):
        self.driver.find_element(By.XPATH, GetHotel.nextPageXpath).click()
        time.sleep(2)

    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(5)

    def see_ability(self):
        self.driver.find_element(By.XPATH, GetHotel.see_abilityXpath).click()

    def resurve_hotel(self):
        self.driver.find_element(By.XPATH, GetHotel.resurbe_hotelXpath).click()

    def scroll_downPage(self):
        self.driver.execute_script("window.scrollBy(0, 500)", "")