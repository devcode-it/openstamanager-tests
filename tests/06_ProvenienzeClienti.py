from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Provenienze_clienti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Anagrafiche")
        self.navigateTo("Provenienze clienti")

    def test_creazione_provenienze_clienti(self):
        # Creazione provenienze clienti      *Required*
        self.creazione_provenienze_clienti("Provenienza Clienti di Prova da Modificare","#9d2929")
        self.creazione_provenienze_clienti("Provenienza Clienti di Prova da Eliminare","#3737db")

        # Modifica provenienza clienti
        self.modifica_provenienze_clienti("Provenienza Clienti di Prova")
        
        # Cancellazione provenienza clienti
        self.elimina_provenienze_clienti()
        
        # Verifica provenienza clienti
        self.verifica_provenienze_clienti()

    def creazione_provenienze_clienti(self, descrizione=str, colore=str):
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        sleep(1)

        self.input(modal, 'Descrizione').setValue(descrizione)
        sleep(1)
        
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_provenienze_clienti(self, modifica=str):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys('Provenienza Clienti di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Provenienze clienti")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_provenienze_clienti(self):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()    

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys('Provenienza Clienti di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_provenienze_clienti(self):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()    

        #verifica elemento modificato
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys("Provenienza Clienti di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Provenienza Clienti di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys("Provenienza Clienti di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)