from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DdtEntrata(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        

    def test_creazione_ddt_entrata(self):
        # Crea un nuovo ddt dal fornitore "Fornitore". *Required*
        importi = RowManager.list()
        self.creazione_ddt_entrata("Fornitore", "1", importi[0])

        # Duplica ddt entrata
        self.duplica_ddt_entrata()

        # Modifica Ddt
        self.modifica_ddt("Evaso")
        
        # Cancellazione Ddt
        self.elimina_ddt()
        
        # Verifica DDT
        self.verifica_ddt()

    def creazione_ddt_entrata(self, fornitore: str, causale: str, file_importi: str):
        self.navigateTo("Ddt in entrata")
        # Crea un nuovo ddt del fornitore indicato.
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Mittente')
        select.setByText(fornitore)

        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def duplica_ddt_entrata(self):
        self.find(By.XPATH, '//button[@class="btn btn-primary ask"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="save"]').click()
        self.wait_loader()

    def modifica_ddt(self, modifica):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Evaso")
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()        
        self.wait_loader()
        
        # Estrazione totali righe
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"]+ ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale"] + ' €'))

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ddt in entrata")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_ddt(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in entrata")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_ddt(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in entrata")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[11]').text
        self.assertEqual("Evaso", self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[11]').text)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
