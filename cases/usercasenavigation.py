import time
from selenium.webdriver.support import expected_conditions as EC 
from artifacts.locatorslogin import Login

class Cases():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Login()

    def navigation(self):
            time.sleep(5)
            self.driver.find_element_by_css_selector(self.locator.bton_dashboard).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.bton_posts).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.bton_site).click()
            time.sleep(3)
    def navigation_addpost(self):
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.bton_posts).click()
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.locator.bton_posts_new).click()
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.locator.posts_create).click()
            self.driver.find_element_by_css_selector(self.locator.posts_create).send_keys("hola este es el post; espero les guste este test automatizado")
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.locator.posts_create_body).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.locator.posts_create_body).send_keys("un ejmplo de mark :) ")
            time.sleep(2)
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.btn_list_publish).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.btn_publish).click()
            self.driver.find_element_by_css_selector(self.locator.btn_publish_modal).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.btn_back_publish).click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.locator.bton_site).click()
            time.sleep(5)
    def navigation_view_post(self):
            self.driver.find_element_by_css_selector(self.locator.bton_site).click()
            time.sleep(2)
            self.open_iframe()
            self.driver.find_element_by_xpath(self.locator.cart_post1).click()
            time.sleep(2)
            self.driver.find_element_by_link_text("Home").click()
            time.sleep(1)
            self.driver.find_element_by_link_text("Collection").click()
            self.close_iframe()
            self.driver.find_element_by_css_selector(self.locator.bton_dashboard).click()
           
        
    def open_iframe(self):
         try:
            iframe = self.driver.find_element_by_css_selector('[class="site-frame "]')
            print('dentro del frame frame-')
            self.driver.switch_to_default_content()
            self.driver.switch_to.frame(iframe)
            
         except Exception as error: 
            print('ERROR------- no entra al frame-')
        
    
    def close_iframe(self):
        try:
            srthandle = self.driver.window_handles
            self.driver.switch_to_window(srthandle[0])
            time.sleep(3)
        except Exception as error:
            print('ERROR--------')


            





       
            
            
