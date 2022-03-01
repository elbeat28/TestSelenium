import time
import unittest
from lib.ma_base_test import MABaseTest
from selenium import webdriver
from cases.usercasenavigation import Cases
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
                                    
URL = 'http://localhost:2368/ghost/#/signin'

class Testweb(MABaseTest):
    
    def setUp(self, url=URL, wait=0):
        super().setUp(url=url, wait=wait)
        self.navigation = Cases(self.driver)
        
    def test_navigation(self):
        self._get_url_and_login()
        self.navigation.navigation()

    def test_navigation_addpost(self):
        self._get_url_and_login()
        self.navigation.navigation_addpost()

    def test_navigation_view_post(self):
        self._get_url_and_login()
        self.navigation.navigation_view_post()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
