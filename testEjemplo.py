import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)


class Testweb(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()
        self.username = self.faker.name()
        # se crea la nueva seccion de crhome
        self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get('https://www.demoblaze.com/index.html')
        self.verificationErrors = []
        self.accept_next_alert = True

    def testSingUpSuccessfull(self):
        self.driver.find_element_by_id("signin2").click()
        time.sleep(2)
        self.driver.find_element_by_id("sign-username").send_keys(self.username)
        self.driver.find_element_by_id("sign-password").send_keys("beat")
        time.sleep(5)
        self.driver.find_element_by_css_selector(
            "#signInModal > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary"
        ).click()
        #la forma de acceder al elemento no es la optima pero hay redundancia en los nombres :(
        time.sleep(5)
        self.assertEqual("Sign up successful.",
                         self.close_alert_and_get_its_text())
        time.sleep(5)

    def login(self):
        self.driver.find_element_by_id("login2").click()
        time.sleep(2)
        self.driver.find_element_by_id("loginusername").clear()
        self.driver.find_element_by_id("loginusername").send_keys("beat9876*")
        self.driver.find_element_by_id("loginpassword").clear()
        self.driver.find_element_by_id("loginpassword").send_keys("beat")
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#logInModal > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary"
        ).click()
        time.sleep(5)

    def testAdd2Phones(self):
        self.login()
        self.driver.find_element_by_link_text("Phones").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Samsung galaxy s6").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Add to cart").click()
        time.sleep(2)
        self.assertEqual("Product added.", self.close_alert_and_get_its_text())
        time.sleep(2)
        #el elemento home no tiene id, ni name lo tuve que traer lo con css selector. no se recomienda usarlo. :(
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Phones").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Iphone 6 32gb").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Add to cart").click()
        time.sleep(2)
        self.assertEqual("Product added.", self.close_alert_and_get_its_text())
        time.sleep(2)
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)

    def testAddLaptops(self):
        self.login()
        self.driver.find_element_by_link_text("Laptops").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("MacBook Pro").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Add to cart").click()
        time.sleep(2)
        self.assertEqual("Product added.", self.close_alert_and_get_its_text())
        time.sleep(2)
        #el elemento home no tiene id, ni name lo tuve que traer lo con css selector. no se recomienda usarlo. :(
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)

    def testAddMonitors(self):
        self.login()
        self.driver.find_element_by_link_text("Monitors").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Apple monitor 24").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Add to cart").click()
        time.sleep(2)
        self.assertEqual("Product added.", self.close_alert_and_get_its_text())
        time.sleep(2)
        #el elemento home no tiene id, ni name lo tuve que traer lo con css selector. no se recomienda usarlo. :(
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)

    def testDeleteProducts(self):
        self.login()
        self.driver.find_element_by_id("cartur").click()
        time.sleep(2)
        #acceder a un elemeto por xpat no se recomieda pero no cuenta con id el elemento :(
        self.driver.find_element_by_xpath(
            "(//a[contains(text(),'Delete')])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "(//a[contains(text(),'Delete')])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)

    def testPayitmesOk(self):
        self.login()
        self.driver.find_element_by_id("cartur").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "button.btn.btn-success").click()
        time.sleep(2)
        self.driver.find_element_by_id("name").send_keys("alberto")
        time.sleep(1)

        self.driver.find_element_by_id("country").send_keys("mexico")
        time.sleep(1)

        self.driver.find_element_by_id("city").send_keys("cdmx")
        time.sleep(2)

        self.driver.find_element_by_id("card").send_keys("4242424242424242")
        time.sleep(1)

        self.driver.find_element_by_id("month").send_keys("10")
        time.sleep(1)

        self.driver.find_element_by_id("year").send_keys("12")
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#orderModal > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "button.confirm.btn.btn-lg.btn-primary").click()
        time.sleep(2)

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        except Exception as e:
            print(e)
        finally:
            self.accept_next_alert = True
            



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
