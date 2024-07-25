from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Adattatori(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")

    def test_creazione_adattatore(self):
        # Creazione marche impianto *Required*
        self.creazione_adattatore("Adattatore di Prova da Modificare", "Archiviazione FTP")
        self.creazione_adattatore("Adattatore di Prova da Eliminare", "Archiviazione FTP")

        # Modifica Adattatore
        self.modifica_adattatore("Adattatore di Prova")
        
        # Cancellazione Adattatore
        self.elimina_adattatore()
        
        # Verifica Adattatore
        self.verifica_adattatore()

    def creazione_adattatore(self, nome: str, tipo: str):
        self.navigateTo("Adattatori di archiviazione")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Tipo archiviazione')
        select.setByText(tipo)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_adattatore(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Adattatore di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)          

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_adattatore(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Adattatore di Prova da Eliminare', Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)          

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_adattatore(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Adattatore di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Adattatore di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Adattatore di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)