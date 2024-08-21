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



class ModelliPrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_modelli_prima_nota(self):
        # Creazione modello prima nota      *Required*
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Modificare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Eliminare", causale="Prova anticipo fattura num. {numero} del {data}")

        # Modifica Modello Prima Nota
        self.modifica_modello_prima_nota("Modello Prima Nota di Prova")
        
        # Cancellazione Modello Prima nota
        self.elimina_modello_prima_nota()
        
        # Verifica Modello Prima nota
        self.verifica_modello_prima_nota()


    def creazione_modelli_prima_nota(self, nome=str, causale=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Causale').setValue(causale)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-conto0-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-conto1-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.wait_loader()

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_modello_prima_nota(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Modello Prima Nota di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)  

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Modelli prima nota")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_modello_prima_nota(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Modello Prima Nota di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def verifica_modello_prima_nota(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Modelli prima nota")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Modello Prima Nota di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Modello Prima Nota di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Modello Prima Nota di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)