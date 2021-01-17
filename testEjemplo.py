import time
import unittest
from models import Customer
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)

from faker import Faker

class Testweb(unittest.TestCase):
    def setUp(self):
        faker = Faker()
        self.customer = Customer(username=faker.name(),
                                 password=faker.password(),
                                 city=faker.city(),
                                 country=faker.country(),
                                 email_address=faker.email(),
                                 year=faker.random_int(21, 26),
                                 credit_card=faker.credit_card_number(),
                                 mouth=faker.random_int(1, 12))
        self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get('https://www.demoblaze.com/index.html')
        self.verificationErrors = []
        self.accept_next_alert = True

    def testhappy_test(self):

        self.register()
        self.login()
        self.navigation()
        self.contact()
        self.about_us()
        self.add_2_phones()
        self.add_laptops()
        self.add_monitors()
        self.delete_products()
        self.pay_itmes()
        self.logout()

    def contact(self):
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Contact").click()
        time.sleep(1)
        self.driver.find_element_by_id("recipient-email").send_keys(
            self.customer.email_address)
        self.driver.find_element_by_id("recipient-name").send_keys(
            self.customer.username)
        self.driver.find_element_by_id("message-text").send_keys(
            "espero les guste mi test automatizado")
        self.driver.find_element_by_css_selector(
            "button.btn.btn-primary").click()
        time.sleep(2)
        self.assertEqual("Thanks for the message!!",
                         self.close_alert_and_get_its_text())
        time.sleep(2)
        self.driver.find_element_by_css_selector("a.nav-link").click()
        time.sleep(2)

    def navigation(self):

        self.driver.find_element_by_css_selector(
            "span.carousel-control-next-icon").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "span.carousel-control-next-icon").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "span.carousel-control-next-icon").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "span.carousel-control-prev-icon").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "span.carousel-control-prev-icon").click()
        time.sleep(2)
        self.driver.find_element_by_id("next2").click()
        time.sleep(2)
        self.driver.find_element_by_id("prev2").click()
        time.sleep(2)

    def about_us(self):
        time.sleep(2)
        self.driver.find_element_by_link_text("About us").click()
        time.sleep(2)
        # no se recomienda usar el xpath pero hay elementos que solo se pueden acceder así :)
        self.driver.find_element_by_xpath(
            "//*[@id='example-video']/div[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='example-video']/div[4]/div[5]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id='example-video']").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#videoModal > div > div > div.modal-footer > button").click()
        time.sleep(2)

    def register(self):
        self.driver.find_element_by_id("signin2").click()
        time.sleep(2)
        self.driver.find_element_by_id("sign-username").send_keys(
            self.customer.username)
        time.sleep(2)
        self.driver.find_element_by_id("sign-password").send_keys(
            self.customer.password)
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
        self.driver.find_element_by_id("loginusername").send_keys(
            self.customer.username)
        self.driver.find_element_by_id("loginpassword").clear()
        self.driver.find_element_by_id("loginpassword").send_keys(
            self.customer.password)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#logInModal > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary"
        ).click()
        time.sleep(5)

    def add_2_phones(self):
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

    def add_laptops(self):
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

    def add_monitors(self):
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
        time.sleep(5)

    def delete_products(self):
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
        time.sleep(5)

    def pay_itmes(self):
        self.driver.find_element_by_id("cartur").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "button.btn.btn-success").click()
        time.sleep(2)
        self.driver.find_element_by_id("name").send_keys(
            self.customer.username)
        time.sleep(1)
        self.driver.find_element_by_id("country").send_keys(
            self.customer.country)
        time.sleep(1)
        self.driver.find_element_by_id("city").send_keys(self.customer.city)
        time.sleep(2)
        self.driver.find_element_by_id("card").send_keys(
            self.customer.credit_card)
        time.sleep(1)
        self.driver.find_element_by_id("month").send_keys(self.customer.mouth)
        time.sleep(1)
        self.driver.find_element_by_id("year").send_keys(self.customer.year)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#orderModal > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "button.confirm.btn.btn-lg.btn-primary").click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element_by_id("logout2").click()
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
