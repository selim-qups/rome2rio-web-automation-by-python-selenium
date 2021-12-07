import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.locators import GetTicketLocatros


class GetTicketPage():
    def __init__(self, driver):
        self.driver = driver

        self.tbtn = GetTicketLocatros.BtnId
        self.inputF = GetTicketLocatros.tinputfromXpath
        self.inputT = GetTicketLocatros.InputToXpath
        self.dDate = GetTicketLocatros.depatureDateXpath
        self.selDate = GetTicketLocatros.DtateselectX
        self.returnDate = GetTicketLocatros.returndateX
        self.returnDSele = GetTicketLocatros.returndateselectX
        self.Sbtn = GetTicketLocatros.searcbtnX

    def ticket_btn(self):
        self.driver.find_element(By.ID, GetTicketLocatros.BtnId).click()
        time.sleep(2)

    def input_f(self, locationfrom):
        self.driver.find_element(By.ID, GetTicketLocatros.tinputfromXpath).send_keys(locationfrom)
        time.sleep(1)

    def input_t(self,locationto):
        self.driver.find_element(By.ID, GetTicketLocatros.InputToXpath).send_keys(locationto)
        time.sleep(5)

    def dDate(self):
        self.driver.find_element(By.XPATH, GetTicketLocatros.depatureDateXpath).click()
        time.sleep(1)

    def dDateSel(self):
        self.driver.find_element(By.XPATH, GetTicketLocatros.DtateselectX).click()
        time.sleep(1)

    def rDate(self):
        self.driver.find_element(By.XPATH, GetTicketLocatros.returndateX).click()
        time.sleep(1)

    def rDateSel(self):
        self.driver.find_element(By.XPATH, GetTicketLocatros.returndateselectX).click()
        time.sleep(1)

    def SubBtn(self):
        self.driver.find_element(By.XPATH, GetTicketLocatros.searcbtnX).click()
        time.sleep(1)

