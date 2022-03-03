import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from cases.usecaseslogin import Cases


class MABaseTest(unittest.TestCase):
    """
    Setup common to all tests.
    """
    def setUp(self, url, wait=3): 
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(wait)
        self.driver.maximize_window()
        self.url = url
        self.login = Cases(self.driver)

    def _get_url_and_login(self):
        self.driver.get(self.url)
        self.login.login()
