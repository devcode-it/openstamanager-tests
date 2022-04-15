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


class Attivita(Test):
    def setUp(self):
        super().setUp()

       
    def test_attivita(self, modifica="3"):
        # Crea un nuovo intervento. 
        importi = RowManager.list()
        self.attivita("Cliente", "1", "2", importi[0])
        self.attivita("Cliente", "1", "2", importi[0])

        # Modifica intervento
        self.navigateTo("Attività")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('1')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Stato').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione intervento
        self.navigateTo("Attività")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('2')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()



    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo("Attività")

        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        self.input(modal, 'Stato').setByIndex(stato)
        
        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto intervento', toast)
        sleep(1)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

        