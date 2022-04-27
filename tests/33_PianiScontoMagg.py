from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PianiScontoMagg(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_piano_sconto_magg(self, modifica="Piano di sconto di Prova"):
        self.navigateTo("Piani di sconto/magg.")
        # Crea un nuovo piano. 
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Modificare", "10")
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Eliminare", "5")

        # Modifica piano di sconto
        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Piano di sconto di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione piano di sconto
        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Piano di sconto di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()



    def creazione_piano_sconto_magg(self, nome: str, sconto: str):
        self.navigateTo("Piani di sconto/magg.")

        # Crea un nuovo piano. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Sconto/magg. combinato').setValue(sconto)


        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto piano', toast)
    
        
        