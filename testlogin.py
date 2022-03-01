import time
import unittest
from lib.ma_base_test import MABaseTest
from selenium import webdriver
from cases.usecaseslogin import Cases
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
                                    
URL = 'http://localhost:2368/ghost/#/signin'

class Testweb(MABaseTest):
    def setUp(self, url=URL, wait=0):
        super().setUp(url=url, wait=wait)
        self.login = Cases(self.driver)
        self.forgotpass = Cases(self.driver)
        self.login_invalid = Cases(self.driver)

    def test_login(self):
        self.driver.get(self.url)
        self.login.login()

    def test_fogot_pass(self):
        self.driver.get(self.url)
        self.login.forgotpass()

    def test_login_invalid(self):
        self.driver.get(self.url)
        self.login.login_invalid()
        
    
     


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
