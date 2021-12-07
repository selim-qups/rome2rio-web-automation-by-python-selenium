from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.get_car_page import GetCarPage

class GetHotelTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_get_car(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        car = GetCarPage(driver)
        car.car_btn()
        car.car_from("Dhaka, Bangladesh")
        car.pickup_date()

    @classmethod
    def tearDownClass(cls):
        print("Succesfully")


if __name__ == '__main__':
    unittest.main()



