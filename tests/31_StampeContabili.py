from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StampeContabili(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Contabilità")
 
    def test_stampecontabili(self):
        # Test stampe contabili
        self.apri_stampe_contabili()

    def apri_stampe_contabili(self):
        self.navigateTo("Stampe contabili")
        self.wait_loader()

        # Stampa registro IVA vendite
        self.find(By.XPATH, '//button[@data-title="Stampa registro IVA vendite"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_sezionale-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_sezionale-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-format-container"]').click()
        self.find(By.XPATH, '//ul[@id="select2-format-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-orientation-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-orientation-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        stampa=self.find(By.XPATH, '//div[@id="viewer"]//span[3]').text
        self.assertEqual(stampa, "REGISTRO IVA VENDITE DAL 01/01/2025 AL 31/12/2025 - STANDARD VENDITE")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Stampa registro IVA acquisti
        self.find(By.XPATH, '//button[@data-title="Stampa registro IVA acquisti"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//span[@id="select2-id_sezionale-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_sezionale-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        stampa=self.find(By.XPATH, '//div[@id="viewer"]//span[3]').text
        self.assertEqual(stampa, "REGISTRO IVA ACQUISTI DAL 01/01/2025 AL 31/12/2025 - STANDARD ACQUISTI")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Stampa liquidazione IVA
        self.find(By.XPATH, '//button[@data-title="Stampa liquidazione IVA"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click() 
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[1]').text 
        self.assertEqual(stampa, "PROSPETTO LIQUIDAZIONE IVA DAL 01/01/2025 AL 31/12/2025")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Stampa Bilancio
        self.find(By.XPATH, '//button[@data-title="Stampa Bilancio"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        stampa=self.find(By.XPATH, '//div[@id="viewer"]//span').text
        self.assertEqual(stampa, "STAMPA BILANCIO")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)
        
        # Stampa Situazione patrimoniale
        self.find(By.XPATH, '(//a[@id="print-button"])[1]').click()
        sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        stampa=self.find(By.XPATH, '//div[@id="viewer"]//span').text
        self.assertEqual(stampa, "STAMPA MASTRINO")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 

        # Stampa Situazione economica
        self.find(By.XPATH, '(//a[@id="print-button"])[2]').click()
        sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[1]').text 
        self.assertEqual(stampa, "STAMPA MASTRINO")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0]) 

        # Stampa fatturato
        self.find(By.XPATH, '(//a[@id="print-button"])[3]').click()
        sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[9]').text 
        self.assertEqual(stampa, "FATTURATO MENSILE DAL 01/01/2025 AL 31/12/2025")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 

        # Stampa acquisti
        self.find(By.XPATH, '(//a[@id="print-button"])[4]').click()
        sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[9]').text 
        self.assertEqual(stampa, "ACQUISTI MENSILI DAL 01/01/2025 AL 31/12/2025")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Stampa libro giornale
        self.find(By.XPATH, '//button[@data-title="Libro giornale"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[1]').text 
        self.assertEqual(stampa, "STAMPA LIBRO GIORNALE")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Stampa scadenziario
        self.find(By.XPATH, '//button[@data-title="Stampa scadenzario"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        stampa=self.find(By.XPATH, '(//div[@id="viewer"]//span)[6]').text  
        self.assertEqual(stampa, "SCADENZE DAL 01/01/2025 AL 31/12/2025")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 
