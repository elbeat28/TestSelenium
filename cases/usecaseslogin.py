import time
from selenium.webdriver.support import expected_conditions as EC 
from artifacts.locatorslogin import Login

class Cases():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Login()
    def login(self):
            time.sleep(4)
            self.driver.find_element_by_css_selector(self.locator.email_textbox).click()
            self.driver.find_element_by_css_selector(self.locator.email_textbox).send_keys("elbeat2810@gmail.com")
            self.driver.find_element_by_css_selector(self.locator.password_textbox).click()
            self.driver.find_element_by_css_selector(self.locator.password_textbox).send_keys("Beat281088*")
            self.driver.find_element_by_css_selector(self.locator.login_button).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.my_account_button).is_displayed()
            self.driver.find_element_by_css_selector(self.locator.my_account_button).click()
            time.sleep(2)
    def forgotpass(self):
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.email_textbox).send_keys("elbeat2810@gmail.com")
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.forgot_button).click()
            time.sleep(2)
            displayed_forgot  = self.driver.find_element_by_css_selector(self.locator.forgot_button)

            if displayed_forgot is True:
	            self.locator.forgot_button.click()
            else:
	            print("no responde el servicio", displayed_forgot)
    def login_invalid(self):
            time.sleep(5)
            self.driver.find_element_by_css_selector(self.locator.email_textbox).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.email_textbox).send_keys("elbeat2810@gmail.com")
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.password_textbox).click()
            self.driver.find_element_by_css_selector(self.locator.password_textbox).send_keys("Beat281088*33333")
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.login_button).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.alert_pss).is_displayed()
            