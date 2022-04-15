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

class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Acquisti")


    def test_creazione_fattura_acquisto(self, modifica = "Modifica di Prova"):
        # Crea una nuova fattura
        importi = RowManager.list()
        self.creazione_fattura_acquisto("Fornitore", "1", "1", importi[0])

        # Modifica fattura
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('1')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        sleep(1)
        self.input(None,'Note').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione fattura
        
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def creazione_fattura_acquisto(self, fornitore: str, numero: str, pagamento: str, file_importi: str):
        self.navigateTo("Fatture di acquisto")

        # Crea una nuova fattura per il fornitore indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'N. fattura del fornitore').setValue(numero)

        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        sleep(1)

        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento')
        select.setByIndex(pagamento)

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto fattura', toast)
        sleep(1)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)
