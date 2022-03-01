import time
import unittest
from lib.ma_base_test import MABaseTest
from selenium import webdriver
from cases.usercasepage_edit import Cases
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
                                    
URL = 'http://localhost:2368/ghost/#/signin'

class Testweb(MABaseTest):
    def setUp(self, url=URL, wait=0):
        super().setUp(url=url, wait=wait)
        self.edit_page = Cases(self.driver)
  

    def test_editpage(self):        
        self._get_url_and_login()
        self.edit_page.edit_page()



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
