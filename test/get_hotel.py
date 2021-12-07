from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from pages.get_hotel_page import GetHotelPage


class GetHotelTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=("D:\Selenium\chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_get_hotel(self):
        driver = self.driver
        driver.get("https://www.rome2rio.com")

        hotel = GetHotelPage(driver)
        hotel.hotel_btn()
        hotel.hotel_location("United Arab Emirats")
        hotel.checkin_Hdate()
        hotel.checkin_date_select()
        driver.get("https://www.booking.com/searchresults.en-gb.html?aid=2097750;label=r2r06%2CINXXX20211204000000000ufod%2Cep01%3Ae%3Aa%3Ad%3Ad%2C%2C8p%3A1%7C8t%3A3%2C202112040000%2C158-20211204-205224-6211541%2C;sid=dcb39031c68ed108d4859e59240adf89;checkin=2021-12-07;checkout=2021-12-09;city=-1456928;highlighted_hotels=7130486;hlrd=with_av;keep_landing=1;redirected=1;source=hotel;srpvid=dade950164840307&room1=A,A,;#hotelTmpl")
        hotel.scroll_page()
        hotel.see_ability()
        driver.get("https://www.booking.com/hotel/fr/paris-j-39-adore-amp-spa.en-gb.html?aid=2097750;label=r2r06%2CINXXX20211204000000000ufod%2Cep01%3Ae%3Aa%3Ad%3Ad%2C%2C8p%3A1%7C8t%3A3%2C202112040000%2C158-20211204-211155-6908897%2C;sid=dcb39031c68ed108d4859e59240adf89;all_sr_blocks=713048601_298165938_0_2_0;checkin=2021-12-05;checkout=2021-12-06;dest_id=-1456928;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=0;highlighted_blocks=713048601_298165938_0_2_0;hpos=0;matching_block_id=713048601_298165938_0_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=713048601_298165938_0_2_0__29504;srepoch=1638653327;srpvid=0b229731901902e7;type=total;ucfs=1&#hotelTmpl")
        hotel.resurve_hotel()

        p = driver.current_window_handle
        child = driver.window_handles
        for window in child:
            if (window == p):
                new_window = driver.switch_to.window(window)

        hotel.scroll_downPage()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)

        print("Succesfully")


if __name__ == '__main__':
    unittest.main()



