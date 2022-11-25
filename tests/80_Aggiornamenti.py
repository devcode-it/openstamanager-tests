from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html


class Aggiornamenti(Test):
    def setUp(self):
        super().setUp()

        
    def test_aggiornamenti(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Aggiornamenti")
        self.wait_loader()    

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info btn-block"]'))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-block"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-block"]'))).click()
        sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()