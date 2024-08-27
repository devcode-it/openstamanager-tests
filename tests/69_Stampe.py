from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Stampe(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")


    def test_stampe(self):
        self.stampe()

    def stampe(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Stampe")
        self.wait_loader()
        
        self.find(By.XPATH, '//tbody//tr//td[2]').click()