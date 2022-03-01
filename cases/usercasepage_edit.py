import time
from selenium.webdriver.support import expected_conditions as EC 
from artifacts.locatorslogin import Login

class Cases():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Login()

    def edit_page(self):
            self.driver.find_element_by_css_selector(self.locator.bton_dashboard).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.edit_page_btn).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.sd_brand).click()
            time.sleep(5)
            self.driver.find_element_by_css_selector(self.locator.sd_description).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.sd_description).clear()
            self.driver.find_element_by_css_selector(self.locator.sd_description).send_keys("Test automatizado")
            time.sleep(2)
            self.driver.find_element_by_css_selector("div.color-box-container > input[name=\"accent-color\"]").click()
            time.sleep(2)
            self.driver.find_element_by_css_selector("div.color-box-container > input[name=\"accent-color\"]").clear()
            time.sleep(2)
            self.driver.find_element_by_css_selector("div.color-box-container > input[name=\"accent-color\"]").send_keys("#98dcd1")
            time.sleep(2)
            self.driver.find_element_by_css_selector("button.gh-nav-design-tab.active").click()
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.locator.sd_site_wide).click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('[name="titleFont"]').click()
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.locator.save).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.settings).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.bton_site).click()
            time.sleep(3)


     
      
            
