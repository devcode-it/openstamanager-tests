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


class FasceOrarie(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Attività")

    def test_creazione_fasce_orarie(self):
        # Creazione fasce orarie *Required*
        self.creazione_fasce_orarie("Fascia Oraria di Prova da Modificare", "8:00", "10:00")
        self.creazione_fasce_orarie("Fascia Oraria di Prova da Eliminare", "8:00", "10:00")

        # Modifica fasce orarie
        self.modifica_fasce_orarie("Fascia Oraria di Prova")

        # Cancellazione fasce orarie
        self.elimina_fasce_orarie()

        # Verifica fasce orarie
        self.verifica_fasce_orarie()

    def creazione_fasce_orarie(self, nome = str, inizio=str, fine=str):
        self.navigateTo("Fasce orarie")
        self.wait_loader()  

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(None,'Ora inizio').setValue(inizio)
        self.input(None,'Ora fine').setValue(fine)
        self.input(modal, 'Nome').setValue(nome)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_fasce_orarie(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fasce orarie")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Fascia Oraria di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Fasce orarie")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_fasce_orarie(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fasce orarie")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Fascia Oraria di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[3]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def verifica_fasce_orarie(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fasce orarie")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Fascia Oraria di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Fascia Oraria di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Fascia Oraria di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)