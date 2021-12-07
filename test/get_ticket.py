from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.get_ticket_page import GetTicketPage


class GetTicketTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_get_ticket(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        ticket = GetTicketPage(driver)

        ticket.ticket_btn()
        ticket.input_f("Dhaka,Bangladesh")
        ticket.input_t("United Arab Emirats")
        ticket.dDate()
        ticket.dDateSel()
        ticket.rDate()
        ticket.rDateSel()
        ticket.SubBtn()

    @classmethod
    def tearDownClass(cls):
        print("Succesfully")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()



