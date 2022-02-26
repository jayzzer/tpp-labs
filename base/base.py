import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class BaseSeleniumTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.setup_driver(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.teardown_driver(cls)

    def setup_driver(self):
        service = ChromeService(ChromeDriverManager().install())

        options = ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def teardown_driver(self):
        self.driver.quit()

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
