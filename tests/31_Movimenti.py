from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Movimenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_movimento(self, modifica="Movimento di Prova"):
        # Crea movimento 
        self.creazione_movimento("10", "Articolo di Prova", "Movimento di Prova")
        self.creazione_movimento("5", "Articolo di Prova", "Movimento di Prova da Eliminare")


        # Cancellazione movimento
        self.navigateTo("Movimenti")
        self.wait_loader()  

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Movimento di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="btn btn-danger btn-xs ask"]/i[@class="fa fa-trash"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()



    def creazione_movimento(self, qta: str, articolo: str, descrizione:str):
        # Crea un nuovo movimento. 
        # Apre la schermata di nuovo elemento
        self.navigateTo("Movimenti")
        self.wait_loader()
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Articolo').setByText(articolo)
        self.input(modal, 'Quantità').setValue(qta)
        self.input(modal, 'Descrizione movimento').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto movimento', toast)
    
        
        